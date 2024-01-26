#!/bin/bash

pid=$(ps -aux | grep IR_filter_switch.py | grep -v grep | awk '{print $2}')

if [ -n "$pid" ]; then
    echo "Python script already running, process id: $pid"
    true
else
    echo "Starting python script"
   python /home/harharpi/IR_filter_switch.py
fi

