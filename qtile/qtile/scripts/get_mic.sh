#!/bin/bash

mute=$(pactl get-source-mute @DEFAULT_SOURCE@ | grep yes)
volume=$(pactl get-source-volume @DEFAULT_SOURCE@ | grep Volume | awk '{print $5}')
 

if [ ! -z "$mute" ]

then
     echo "[X]"
else
     echo "[$volume]"
fi
exit 0
