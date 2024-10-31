# Setup new Macbook Pro laptop for development

## Utilities

- Move and resize windows in macOS using keyboard shortcuts - [Rectangle](https://rectangleapp.com/)
- Clipboard manager for developers - [Flycut](http://github.com/TermiT/flycut)

## Homebrew

Install the _[Homebrew](https://brew.sh/)_ package manager. This will allow you to install almost any app from the command line.

```bash
  # install
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

  # update
  brew update
```

Once this is done, install the following via Homebrew. Some of the installers will have additional steps (e.g. add program to PATH), make sure to follow them.

| Package | Usage                                                                                     |
| ------- | ----------------------------------------------------------------------------------------- |
| Colima  | Docker container runtimes on macOS (and Linux) [link](https://github.com/abiosoft/colima) |
| glab    | Gitlab CLI [link](https://gitlab.com/gitlab-org/cli)                                      |
| trivy   | Image security scan CLI [link](https://github.com/aquasecurity/trivy)                     |

```bash
  # Core
  brew install \
    iterm2 \
    make \
    nvm \
    kubectx \
    pyenv \
    colima \
    glab \
    trivy


  # Cask
  brew install --cask \
    docker \
    postman \
    sublime-text \
    visual-studio-code \
    intellij-idea-ce \
    google-cloud-sdk
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

# Java

Stress-free way to manage JDK - https://sdkman.io/

## Git

Configure Git

```bash
git config --global user.name "FIRST_NAME LAST_NAME" --global user.email "MY_NAME@email.com"
```

If you need to configure git for a single repository, replace `--global` flag with `--local`

Credit to https://ma.ttias.be/pretty-git-log-in-one-line/

```bash
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

## Kubernetes

Faster way to switch between clusters and namespaces in kubectl
https://github.com/ahmetb/kubectx?tab=readme-ov-file
