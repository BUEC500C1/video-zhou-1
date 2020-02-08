#! /bin/bash    

# example code: 
# to change the bitrate of the video, you would use it like this:   
# ffmpeg -i input.webm -c:a copy -c:v vp9 -b:v 1M output.mkv    

# resource from: https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats     

# Use FFmpeg to re-encode a video file (MOV, or MP4) to two bitrates     
# Basic conversion, Selecting your codecs, Changing a single stream,      
# Influencing the quality (adjust the frame rate of the video using the -r option; adjust the dimensions of your video; change the bitrate of the video)      
ffmpeg -i input.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M output.mp4
ffmpeg -i input.mp4 -c:a copy -c:v copy -r 30 -s hd480 -b:v 1M output.mp4
