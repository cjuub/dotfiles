#
# ~/.bash_profile
#

export XGD_CONFIG_HOME=~/.config
export XGD_DATA_HOME=~/.local/share
export XDG_DOCUMENTS_DIR=~/documents

export TERMINAL=/bin/termite

[[ -f ~/.bashrc ]] && . ~/.bashrc

# MPD daemon start (if no other user instance exists)
[ ! -s ~/.config/mpd/pid ] && mpd ~/.config/mpd/mpd.conf

if [ -z "$DISPLAY" ] && [ -n "$XDG_VTNR" ] && [ "$XDG_VTNR" -eq 1 ]; then
  exec startx
fi

