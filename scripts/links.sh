#!/usr/bin/env bash

case "$1" in
jira) open -a "Google Chrome" 'https://www.atlassian.com/software/jira';;
custom1) open -a "Google Chrome" 'https://www.atlassian.com/software/jira'$2;;
password) open -a "Google Chrome" 'https://www.grc.com/passwords.htm';;

*) echo "No arguments"
esac