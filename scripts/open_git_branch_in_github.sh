#! /bin/bash

BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)
REPOSITORY_URL=$(git remote -v | grep git@github.com | grep fetch | head -1 | cut -f2 | cut -d' ' -f1 | sed -e 's/:/\//' -e 's/git@/http:\/\//' | sed 's/.git$//g')
REPOSITORY_BRANCH_URL="$REPOSITORY_URL/tree/$BRANCH_NAME"

open -a "Google Chrome" $REPOSITORY_BRANCH_URL