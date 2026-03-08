---
name: pii-scrubber
description: Ensures that any code handling Personally Identifiable Information (PII) includes proper scrubbing and anonymisation techniques.
user-invokable: false
compatibility: python, typescript, kotlin, yaml, bash, .env

---

1. run regex checks (included in pii-regex.md) to identify potential PII in the codebase.
2. If potential PII is found, suggest implementing scrubbing techniques such as:
   - Masking: Replace sensitive data with a fixed character (e.g., `****`).
   - Hashing: Use a secure hashing algorithm to anonymize data (e.g., SHA-256).
   - Tokenization: Replace sensitive data with non-sensitive placeholders (e.g., `<EMAIL_ADDRESS>`).
3. Ensure that any code handling PII follows best practices for data protection, such as:
   - Avoiding logging of PII.
   - Implementing access controls to restrict who can view or modify PII.