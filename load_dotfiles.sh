#!/bin/bash

cp -v .bash_profile ~/.bash_profile
cp -v .bashrc ~/.bashrc
cp -v .vimrc ~/.vimrc
cp -v .xbindkeysrc ~/.xbindkeysrc
cp -v .xinitrc ~/.xinitrc

mkdir -p ~/.config

cp -v .config/compton.conf ~/.config/compton.conf

mkdir -p ~/.config/i3
mkdir -p ~/.config/i3status
mkdir -p ~/.config/mpd
mkdir -p ~/.config/ncmpcpp
mkdir -p ~/.config/ranger
mkdir -p ~/.config/screencloud
mkdir -p ~/.config/termite

cp -rv .config/i3 ~/.config/
cp -rv .config/i3status ~/.config/
cp -v .config/mpd/mpd.conf ~/.config/mpd/mpd.conf
cp -rv .config/ncmpcpp ~/.config/ncmpcpp/
cp -v .config/ranger/rc.conf ~/.config/ranger/rc.conf
cp -v .config/ranger/commands.py ~/.config/ranger/commands.py
cp -v .config/screencloud/ScreenCloud.conf ~/.config/screencloud/ScreenCloud.conf
cp -v .config/termite/config ~/.config/termite/config

