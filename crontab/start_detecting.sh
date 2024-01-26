#!/bin/bash

pid=$(ps -aux | grep sound_detect.sh | grep -v grep | awk '{print $2}')

if [ -n "$pid" ]; then
    echo "Already running"
    true
else
    echo "Starting script to detect noises
   sound_detect.sh
fi


