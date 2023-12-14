#include <stdlib.h>
#include <stdio.h>
 int main()
 {
    int video = system("libcamera-vid --codec libav --libav-audio --audio-device 3,0 -t 10000 -o test.mp4 --width 1920 --height 1080");


    return video;
 }
