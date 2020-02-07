# test code from https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python   

#!/usr/bin/env python3

import multiprocessing
import threading
import time
import sys

def cpu_func(result, niters):
    '''
    A useless CPU bound function.
    '''
    for i in range(niters):
        result = (result * result * i + 2 * result * i * i + 3) % 10000000
    return result

class CpuThread(threading.Thread):
    def __init__(self, niters):
        super().__init__()
        self.niters = niters
        self.result = 1
    def run(self):
        self.result = cpu_func(self.result, self.niters)

class CpuProcess(multiprocessing.Process):
    def __init__(self, niters):
        super().__init__()
        self.niters = niters
        self.result = 1
    def run(self):
        self.result = cpu_func(self.result, self.niters)

class IoThread(threading.Thread):
    def __init__(self, sleep):
        super().__init__()
        self.sleep = sleep
        self.result = self.sleep
    def run(self):
        time.sleep(self.sleep)

class IoProcess(multiprocessing.Process):
    def __init__(self, sleep):
        super().__init__()
        self.sleep = sleep
        self.result = self.sleep
    def run(self):
        time.sleep(self.sleep)



        
