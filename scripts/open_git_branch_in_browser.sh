#! /bin/bash

BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

RAW_REPOSITORY_URL=$(git remote -v | grep .com | grep fetch | head -1 | cut -f2 | cut -d' ' -f1)
if [[ $RAW_REPOSITORY_URL == "git@"* ]]; then
  REPOSITORY_URL=$(echo $RAW_REPOSITORY_URL | sed -e 's/:/\//' -e 's/git@/https:\/\//' | sed 's/.git$//g')
else
  REPOSITORY_URL=$(echo $RAW_REPOSITORY_URL | sed 's/.git$//g')
fi

URL_PATH=""

# ci
if [[ "$1" == "ci" ]] && [[ "$REPOSITORY_URL" == *"gitlab"* ]]; then
    URL_PATH="-/pipelines"
elif [[ "$1" == "ci" ]] && ! [[ "$REPOSITORY_URL" == *"gitlab"* ]]; then
    URL_PATH="actions"

# branch
elif [[ -z "$1" ]] && [[ "$REPOSITORY_URL" == *"gitlab"* ]]; then
  URL_PATH="-/tree/$BRANCH_NAME"
elif [[ -z "$1" ]] && ! [[ "$REPOSITORY_URL" == *"gitlab"* ]]; then
  URL_PATH="tree/$BRANCH_NAME"
fi

open -a "Google Chrome" "$REPOSITORY_URL/$URL_PATH"