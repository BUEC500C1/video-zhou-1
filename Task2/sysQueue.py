# !/usr/bin/env python3
'''
Copyright @2020 Zhou Shen
HW 4 - #0
'''

import queue
import time
import multiprocessing
import threading

from tweepyInfo import tweepy_info
from imgToVideo import imgToVideo

# test 
keyNames = ['BU_ece', 'BU_CCD', 'BU_CAS', 'BU_Tweets', 'realDonaldTrump', 'BarackObama', 'RealTonyStark', '_Spiderman', 'amazon', 'Google', 'Microsoft', 'LinkedIn']

# Build threads
num_threads = 4
threads = []


# build queue
q = queue.Queue()


def worker():
  while True:
    item = q.get()

    numb = 0
    qSize = q.qsize()
    if item is None:
      print("No item now, please put in some stuff!")
      numb = 0
      break

    numb += 1
    print("Currently process on " + str(numb) + " from current " + str(qSize) + " items")
    #do_work(item)
    # after get all images, then get videos
    tweepy_info(item) 
    imgToVideo(item)

    print("Current worker is finished.")
    
    q.task_done()



# put items in queue
for item in keyNames:
  q.put(item)
# how to wait for enqueued tasks to be completed
# reference: https://docs.python.org/2/library/queue.html  
for i in range(num_threads):
  t = threading.Thread(target=worker)
  t.daemon = True
  t.start()
  threads.append(t)
# Blocks until all items in the queue have been gotten and processed.
q.join() 


# put threads in queue
for i in range(num_threads):
  q.put(None)
# join thread in threads list
for j in threads:
  t.join()

