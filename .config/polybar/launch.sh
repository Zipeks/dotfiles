#!/usr/bin/env bash

THEME="idiot_nerd"

killall polybar
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

CONFIG_DIR=/home/mateusz/.config/polybar/$THEME/config.ini
#polybar main -c $CONFIG_DIR &
polybar Virtual1 -c $CONFIG_DIR &
polybar Virtual2 -c $CONFIG_DIR &