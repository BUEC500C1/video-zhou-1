#! /bin/bash    

# example code
ffmpeg -i input.mp4 -strict -2 -vcodec h264 output.mp4  

ffmpeg -i input.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M output.mp4
ffmpeg -i input.mp4 -c:a copy -c:v copy -r 30 -s hd480 -b:v 1M output.mp4
