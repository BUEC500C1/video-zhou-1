import os
import subprocess

# current folder
os.chdir('.')

# convert jpg to mp4
# ffmpeg -i img-%02d.png video_name.avi #2-digit number for name
# set frame rate
subprocess.call(['ffmpeg', '-framerate', '15', '-i', '%01d.jpg', 
  'normal.avi'])

# command line: 
# ffmpeg -i input.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M output.mp4
subprocess.call(['ffmpeg', '-i', 'normal.avi', '-c:a', 'copy', 
  '-c:v', 'copy', '-r', '30', '-s', 'hd720', '-b:v', '2M', 
  'better.mp4'])


# convert mp4 to gif
# subprocess.call(['ffmpeg', '-i', 'output.mp4', '-t', '5', 'out.gif'])

try:
    f1 = open("output.mp4")
    f2 = open("test.mp4")
except IOError:
    print("File(s) not accessible")
finally:
    f1.close()
    f2.close()
