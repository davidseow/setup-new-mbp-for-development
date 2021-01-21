# Setup new Macbook Pro laptop for development

## Install via App Store

- XCode
- Magnet / [Spectacle](https://www.spectacleapp.com/)

## Homebrew

Install the _[Homebrew](https://brew.sh/)_ package manager. This will allow you to install almost any app from the command line.

```bash
  # install
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

  # update
  brew update
```

Once this is done, install the following via Homebrew:

```bash
  # Core
  brew install \
    iterm2 \
    git \
    make \
    nvm \
    spectacle \


  # Cask
  brew install --cask \
    docker \
    firefox \
    google-chrome \
    google-chrome-canary \
    postman \
    slack \
    sublime-text \
    visual-studio-code
```

## Shell

### ohmyzsh

```bash
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Automatically switch to project node version

https://github.com/nvm-sh/nvm#calling-nvm-use-automatically-in-a-directory-with-a-nvmrc-file

### Terminal aliases

```bash
  alias gp="git pull"
  alias gc="git checkout"
  alias gs="git status"
  alias gpr="git pull --rebase"
  alias gh="<path_to_this_repository>/scripts/open_git_branch_in_github.sh
```

## Node Version Manager

```bash
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash
```

## Customise Touchbar

```bash
  brew cask install mtmr
```

To customise touchbar see: https://github.com/Toxblh/MTMR
