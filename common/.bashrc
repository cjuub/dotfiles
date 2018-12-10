#!/usr/bin/env bash

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1="\[\033[38;5;80m\][\[$(tput sgr0)\]\[\033[38;5;219m\]\u@\h\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]\[\033[38;5;80m\]\w]\[$(tput sgr0)\]\[\033[38;5;219m\]\\$\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"

