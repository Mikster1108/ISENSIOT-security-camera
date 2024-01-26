#!/bin/bash

pid=$(ps -aux | grep libcamerify | grep -v grep | awk '{print $2}')

if [ -n "$pid" ]; then
    echo "Already running motion"
    true
else
    echo "Starting motion"
         sudo libcamerify motion 
fi




