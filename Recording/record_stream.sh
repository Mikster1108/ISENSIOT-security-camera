                                                                                  
#!/bin/bash

stream_url="http://192.168.102.25:8089/0/stream" 
timestamp=$(date +"%Y%m%d_%H%M%S")
output_file="output_${timestamp}.mp4"

ffmpeg -i "$stream_url" -t 10 -c:v libx264 -preset ultrafast -c:a aac -strict experimental "$output_file"







