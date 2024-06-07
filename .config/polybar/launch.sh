#!/usr/bin/env bash

THEME="idiot_nerd"

killall -q polybar
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

CONFIG_DIR=~/.config/polybar/$THEME/config.ini
#CONFIG_DIR = ~/.config/polybar.old/config.ini
#polybar main -c $CONFIG_DIR &
polybar DP-2 -c $CONFIG_DIR &
polybar DP-0 -c  $CONFIG_DIR &
