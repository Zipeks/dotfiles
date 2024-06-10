#!/bin/bash

source ~/.screenlayout/default.sh 
nvidia-settings --load-config-only
# Apply wallpaper using wal
nitrogen --restore &

# Start picom
picom --config ~/.config/picom/picom.conf &

setxkbmap -option caps:escape &