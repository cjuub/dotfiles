#!/bin/sh

sleep $1

DVI_5_STATUS=$(</sys/class/drm/card0-DP-5/status )  
DVI_6_STATUS=$(</sys/class/drm/card0-DP-6/status )  
DVI_7_STATUS=$(</sys/class/drm/card0-DP-7/status )  

if [ "connected" == "$DVI_5_STATUS" ] || [ "connected" == "$DVI_6_STATUS" ] || [ "connected" == "$DVI_7_STATUS" ]; then  
    /usr/bin/xrandr --output DP1-2 --off
    /usr/bin/xrandr --output DP1-2 --auto --output eDP1 --off 
    /usr/bin/echo "Xft.dpi: 96" >> $HOME/.Xresources 
else  
    /usr/bin/xrandr --output DP1-2 --off --output eDP1 --auto 
    /usr/bin/echo "Xft.dpi: 192" >> $HOME/.Xresources 
fi

/usr/bin/xrdb -merge $HOME/.Xresources 
/usr/bin/i3 restart
$HOME/.fehbg

sleep 5
/usr/bin/setxkbmap us -variant altgr-intl -option caps:super

