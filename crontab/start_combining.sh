#!/bin/bash

pid=$(ps -aux | grep combine_audio_with_video.sh | grep -v grep | awk '{print $2}')

if [ -n "$pid" ]; then
    echo "Already running"
    true
else
    echo "Starting script to combine audio with video"
   sudo ./combine_audio_with_video.sh > /dev/null &
fi


