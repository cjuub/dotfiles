#!/bin/bash

(setxkbmap -query | grep -q "layout:\\s\\+us") && setxkbmap se -option caps:super || setxkbmap us -option caps:super

