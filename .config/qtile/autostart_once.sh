#!/bin/bash

# source ~/.screenlayout/default.sh
xrandr --output DP-2 --primary --mode 2560x1440 --rate 144 --rotate normal --output DP-0 --mode 1920x1080 --rate 75 --rotate normal --left-of DP-2
nvidia-settings --load-config-only
# Apply wallpaper using wal
nitrogen --restore &


greenclip daemon &
# Start picom
picom --config ~/.config/picom/picom.conf &

setxkbmap -option caps:escape &