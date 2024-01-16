#!/bin/bash

video_filename="$1"

filename=$(basename "$video_filename" | cut -d. -f1)
output_file="audio_${filename}"
output_folder="/home/harharpi/audio_video_files"

if [ -e "$output_file.wav" ]; then
        echo "script already running"
        exit 1

fi
pkill -f "audio.py"
sleep 5
arecord -D plughw:3,0 -f cd -t wav -r 44100 "$output_folder/$filename.wav"


