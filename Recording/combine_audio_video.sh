#!/bin/bash

input_folder_path="/home/harharpi/audio_video_files"
output_folder_path="/home/harharpi/video_files"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder_path"

for video in "$input_folder_path"/*.mp4; do
    # Extract timestamp from video filename
    timestamp=$(basename "$video" | sed -n 's/.*\([0-9]\{2\}-[0-9]\{2\}-[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}-[0-9]\{2\}\).*/\1/p')
    
    # Check if there are matching audio files for each video
    audio="${input_folder_path}/${timestamp}.wav"
    
    if [ -e "$audio" ]; then
        filename_noext="${timestamp}"
        output="$output_folder_path/${filename_noext}.mp4"
        ffmpeg -i "$video" -i "$audio" -c:v copy -c:a aac -shortest -strict experimental "$output"
        # Delete the audio and video files from the input folder after merging
        sudo rm $video
        sudo rm $audio
    else
        echo "Warning: No matching audio file found for $video"
    fi
done