#!/bin/bash

pid_file="/tmp/recordaudio_pid.txt"

if [ -e "$pid_file" ]; then
        pid=$(cat "$pid_file")
        kill -TERM "$pid"
        sudo rm "$pid_file"

else
        echo "Can't find PID file"
fi 

