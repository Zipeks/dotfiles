#!/bin/sh
#by xpander
#path to config file
# CONF_PATH="picom.conf"
 
# Toggle part
CHECK=`ps -aux | grep picom | grep -v grep | wc -l`
if [ $CHECK == "2" ]; then
    picom &
else
    pkill picom
fi