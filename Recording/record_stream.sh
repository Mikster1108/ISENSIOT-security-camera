#!/bin/bash

IP=$(hostname -I | awk '{print $1}')
stream_url="http://${IP}:8089/0/stream"

timestamp=$(date +"%d-%m-%Y-%H-%M-%S")
output_video="${timestamp}.mp4"
output_audio="${timestamp}.wav"
output_folder="/home/harharpi/audio_video_files"

another_instance()
{
        echo "already running, exiting"
        exit 1
}

if [ "$(pgrep recordstream.sh)" != $$ ]; then
     another_instance
fi

echo 'Starting recording' 
ffmpeg -i "$stream_url" -t 90 -c:v libx264 -preset ultrafast -c:a aac -strict experimental "$output_folder/$output_video" & arecord -Dplug:dsnoop -f cd -t wav -r 44100 -d 90 "$output_folder/$output_audio"

echo "File saved as $output_video"





