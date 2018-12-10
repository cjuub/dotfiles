#!/usr/bin/env zsh

# oh-my-zsh
ZSH=/usr/share/oh-my-zsh/
ZSH_THEME="minimal"
source $ZSH/oh-my-zsh.sh

# enable syntax highlighting
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# vim mode
bindkey -v

setopt autocd extendedglob nomatch
unsetopt appendhistory notify beep

# history
HISTFILE=~/.histfile
HISTSIZE=10000
SAVEHIST=10000

# The following lines were added by compinstall
zstyle :compinstall filename $HOME/.zshrc
autoload -Uz compinit
compinit
# End of lines added by compinstall

