#!/bin/bash

# source ~/.screenlayout/default.sh
# Apply wallpaper using wal
nitrogen --restore &


greenclip daemon &
# Start picom
picom --config ~/.config/picom/picom.conf &
syncthing &
setxkbmap -option caps:escape &
systemctl --user enable opentabletdriver.service --now &
playerctld daemon &