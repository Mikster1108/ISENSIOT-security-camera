#!/bin/bash

#takes the filename of the video that motion started recording upon detecting movement
video_filename="$1"

filename=$(basename "$video_filename" | cut -d. -f1)
output_folder="/home/harharpi/audio_video_files"

if [ -e "$filename.wav" ]; then
        echo "script already running"
        exit 1

fi
echo $$ > /tmp/recordaudio_pid.txt
arecord -Dplug:dsnoop -f cd -t wav -r 44100 "$output_folder/$filename.wav"

