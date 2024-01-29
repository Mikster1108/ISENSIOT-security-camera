#!/bin/bash

IP=$(hostname -I | awk '{print $1}')
stream_url="http://${IP}:8089/0/stream"

timestamp=$(date +"%d-%m-%Y-%H-%M-%S")
output_video="${timestamp}.mp4"
output_audio="${timestamp}.wav"
output_folder="/home/harharpi/audio_video_files"

#sound threshold
min_sound_threshold=2


# Function to handle cleanup on exit
cleanup() {
    echo "Exiting..."
    rm -f /dev/shm/noise.wav
    exit
}

# Trap Ctrl+C (SIGINT) and call the cleanup function
trap cleanup INT


while true; do
    arecord -Dplug:dsnoop -f cd -t wav -d 2 -r 16000 /dev/shm/noise.wav
    volume=$(sox /dev/shm/noise.wav -n stats -s 16 2>&1 | awk '/^Max\ level/ {print int($3)}')
    noise=$(echo "$volume > $threshold" | bc -l)
        echo "current volume: $volume"

    if [ "$noise" -eq 1 ]; then
        ffmpeg -i "$stream_url" -t 30 -c:v libx264 -preset ultrafast -c:a aac -strict experimental "$output_folder/$output_video" & arecord -Dplug:dsnoop -f cd -t wav -r 44100 -d 30 "$output_folder/$output_audio"
    fi
done
