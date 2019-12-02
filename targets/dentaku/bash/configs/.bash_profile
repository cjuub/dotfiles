#!/usr/bin/env bash

source $HOME/.env

[[ -f ~/.bashrc ]] && . ~/.bashrc

# Set up automatic sync for keepass file
~/documents/private/keepass_sync.sh &

if [ -z "$DISPLAY" ] && [ -n "$XDG_VTNR" ] && [ "$XDG_VTNR" -eq 1 ]; then
  exec startx
fi

