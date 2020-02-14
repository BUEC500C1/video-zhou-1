import os
import subprocess

# current folder
os.chdir('.')

# convert jpg to mp4
subprocess.call(['ffmpeg', '-i', 'earth.jpg', 'output.mp4'])
# command line: 
# ffmpeg -i input.mp4 -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M output.mp4
subprocess.call(['ffmpeg', '-i', 'output.mp4', '-c:a', 'copy', 
  '-c:v', 'copy', '-r', '30', '-s', 'hd720', '-b:v', '2M', 
  'test.mp4'])


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
