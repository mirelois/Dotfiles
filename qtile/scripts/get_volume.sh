#!/bin/bash

mute=$(pactl get-sink-mute @DEFAULT_SINK@ | grep yes)
volume=$(pactl get-sink-volume @DEFAULT_SINK@ | grep Volume | awk '{print $5}')
 

if [ ! -z "$mute" ]

then
     echo "[X]"
else
     echo "[$volume]"
fi
exit 0
