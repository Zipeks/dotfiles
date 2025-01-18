#!/bin/bash

# source ~/.screenlayout/default.sh
# Apply wallpaper using wal
xrandr --output DP-4 --primary --mode 2560x1440 --rate 144 --rotate normal --output DP-2 --mode 1920x1080 --rate 75 --rotate normal --left-of DP-4 &
nitrogen --restore &


greenclip daemon &
# Start picom
picom --config ~/.config/picom/picom.conf &
syncthing &
setxkbmap -option caps:escape &
systemctl --user enable opentabletdriver.service --now &
playerctld daemon &