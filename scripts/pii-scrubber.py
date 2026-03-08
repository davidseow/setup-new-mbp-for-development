#!/usr/bin/env python3
"""
PII Scrubber - Detects Personally Identifiable Information in git changes.

Reads regex patterns from pii-config.json and scans changed files in git
for matches. Reports findings with file path, line number, and PII type.
"""

import json
import re
import subprocess
import sys
import os
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class PII_Finding:
    """Represents a detected PII instance."""
    file: str
    line_number: int
    pii_type: str
    context: str


def load_patterns(config_path: str) -> List[Dict]:
    """Load PII regex patterns from config file."""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            return config.get('patterns', [])
    except FileNotFoundError:
        print(f"Error: Configuration file not found: {config_path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in configuration file: {config_path}", file=sys.stderr)
        sys.exit(1)


def get_changed_files() -> List[str]:
    """Get list of changed files from git diff (both staged and unstaged)."""
    try:
        changed_files = set()
        
        # Get staged changes (--cached)
        result = subprocess.run(
            ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR'],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0 and result.stdout:
            changed_files.update(f.strip() for f in result.stdout.strip().split('\n') if f.strip())
        
        # Get unstaged changes
        result = subprocess.run(
            ['git', 'diff', '--name-only', '--diff-filter=ACMR'],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0 and result.stdout:
            changed_files.update(f.strip() for f in result.stdout.strip().split('\n') if f.strip())
        
        return list(changed_files)
    except FileNotFoundError:
        print("Error: git command not found. Are you in a git repository?", file=sys.stderr)
        return []


def should_skip_file(file_path: str) -> bool:
    """Check if file should be skipped (binary files, etc.)."""
    binary_extensions = {'.bin', '.exe', '.jpg', '.png', '.gif', '.pdf', '.zip', '.tar', '.gz'}
    extension = Path(file_path).suffix.lower()
    
    if extension in binary_extensions:
        return True
    
    # Skip deleted files
    if not os.path.exists(file_path):
        return True
    
    return False


def scan_file_for_pii(file_path: str, patterns: List[Dict]) -> List[PII_Finding]:
    """Scan a file for PII matches."""
    findings = []
    
    if should_skip_file(file_path):
        return findings
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
        return findings
    
    for line_number, line in enumerate(lines, 1):
        for pattern in patterns:
            try:
                regex = re.compile(pattern['regex'], re.IGNORECASE)
                matches = regex.finditer(line)
                
                for match in matches:
                    # Extract context (surrounding text, truncated)
                    context = line.strip()
                    if len(context) > 60:
                        start = max(0, match.start() - 20)
                        end = min(len(line), match.end() + 20)
                        context = line[start:end].strip()
                        if start > 0:
                            context = "..." + context
                        if end < len(line):
                            context = context + "..."
                    
                    findings.append(PII_Finding(
                        file=file_path,
                        line_number=line_number,
                        pii_type=pattern['name'],
                        context=context
                    ))
            except re.error as e:
                print(f"Warning: Invalid regex for {pattern['name']}: {e}", file=sys.stderr)
                continue
    
    return findings


def print_findings(findings: List[PII_Finding]) -> None:
    """Print findings in human-readable table format."""
    if not findings:
        return
    
    # Sort by file and line number
    findings.sort(key=lambda x: (x.file, x.line_number))
    
    # Calculate column widths
    max_file_len = max(len(f.file) for f in findings) if findings else 10
    max_type_len = max(len(f.pii_type) for f in findings) if findings else 15
    max_context_len = 50
    
    # Ensure minimum widths
    max_file_len = max(max_file_len, 20)
    max_type_len = max(max_type_len, 15)
    
    # Print header
    print("-" * (max_file_len + max_type_len + max_context_len + 20))
    print(f"{'File':<{max_file_len}} | {'Line':<6} | {'Type':<{max_type_len}} | {'Context':<{max_context_len}}")
    print("-" * (max_file_len + max_type_len + max_context_len + 20))
    
    # Print findings
    for finding in findings:
        context = finding.context[:max_context_len]
        if len(finding.context) > max_context_len:
            context = context[:-3] + "..."
        
        print(f"{finding.file:<{max_file_len}} | {finding.line_number:<6} | {finding.pii_type:<{max_type_len}} | {context:<{max_context_len}}")
    
    print("-" * (max_file_len + max_type_len + max_context_len + 20))


def main():
    """Main entry point."""
    # Determine config file path
    script_dir = Path(__file__).parent
    config_path = script_dir / 'pii-config.json'
    
    patterns = load_patterns(str(config_path))
    
    if not patterns:
        print("Error: No patterns loaded from configuration", file=sys.stderr)
        sys.exit(1)
    
    # Get changed files from git
    changed_files = get_changed_files()
    
    if not changed_files:
        print("No changed files found.")
        sys.exit(0)
    
    all_findings = []
    
    # Scan each changed file
    for file_path in changed_files:
        findings = scan_file_for_pii(file_path, patterns)
        all_findings.extend(findings)
    
    # Print results
    if all_findings:
        print(f"\n⚠️  Found {len(all_findings)} potential PII match(es):\n")
        print_findings(all_findings)
        print(f"\nTotal findings: {len(all_findings)}")
        sys.exit(1)
    else:
        print("✓ No PII detected in changed files.")
        sys.exit(0)


if __name__ == '__main__':
    main()
