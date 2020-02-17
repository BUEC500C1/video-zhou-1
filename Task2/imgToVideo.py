# !/usr/bin/env python3
'''
Copyright @2020 Zhou Shen
HW 4 - #3
'''

import os
import subprocess

def imgToVideo(twitterUsr):
  fileName = "img/" + twitterUsr + "%01d" + ".png"
  normalVideo = "output/" + twitterUsr + "normal.avi"
  betterVideo = "output/" + twitterUsr + "better.mp4"

  # convert jpg to mp4
  # ffmpeg -i img-%02d.png video_name.avi #2-digit number for name
  # set frame rate
  # ffmpeg -framerate 30 -i img%03d.png output.mp4  
  subprocess.call(['ffmpeg', '-framerate', '1', '-i', 
    fileName, 
    normalVideo])

  # convert to better quality
  subprocess.call(['ffmpeg', '-i', normalVideo, '-c:a', 'copy', 
    '-c:v', 'copy', '-r', '30', '-s', 'hd720', '-b:v', '2M', 
    betterVideo])

## test use only
# imgToVideo("BU")