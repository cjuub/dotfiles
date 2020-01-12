#!/bin/bash

if xinput list-props 12 | grep "Device Enabled (141).*1" >/dev/null
then
  #xinput disable 12
  sudo modprobe -r hid_generic
  sudo modprobe -r hid_multitouch
else
  #xinput enable 12
  sudo modprobe hid_multitouch
  sleep 1
  # touchpad tap click enable
  xinput set-prop 13 297 1
  # touchpad speed
  xinput set-prop 13 288 0.5
  # touchpad natural scroll enable
  xinput set-prop 13 281 1
fi
