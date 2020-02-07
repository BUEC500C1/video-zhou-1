Python threading    
https://docs.python.org/3/library/threading.html    
Thread-based parallelism     
This module constructs higher-level threading interfaces on top of the lower level _ thread module.     

Thread-local data is data whose values are thread specific. To manage thread-local data, just create an instance of local (or a subclass) and store attributes on it:    
```
mydata = threading.local()   
mydata.x = 1    
```

Thread Objects    
The Thread class represents an activity that is run in a separate thread of control. There are two ways to specify the activity: by passing a callable object to the constructor, or by overriding the run() method in a subclass.      

Lock Objects    
A primitive lock is a synchronization primitive that is not owned by a particular thread when locked. In Python, it is currently the lowest level synchronization primitive available, implemented directly by the _ thread extension module.      

RLock Objects    
A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread.    

Condition Objects    
A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. Passing one in is useful when several condition variables must share the same lock. The lock is part of the condition object: you don’t have to track it separately.     

Semaphore Objects    
This is one of the oldest synchronization primitives in the history of computer science, invented by the early Dutch computer scientist Edsger W. Dijkstra (he used the names P() and V() instead of acquire() and release()).     

Event Objects     
This is one of the simplest mechanisms for communication between threads: one thread signals an event and other threads wait for it.   

Timer Objects   
This class represents an action that should be run only after a certain amount of time has passed — a timer. Timer is a subclass of Thread and as such also functions as an example of creating custom threads.     

Barrier Objects     
New in version 3.2.     
This class provides a simple synchronization primitive for use by a fixed number of threads that need to wait for each other.     
```
b = Barrier(2, timeout=5)

def server():
    start_server()
    b.wait()
    while True:
        connection = accept_connection()
        process_server_connection(connection)

def client():
    b.wait()
    while True:
        connection = make_connection()
        process_client_connection(connection)
```


Multiprocessing vs Threading Python     
https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python    
1. The threading module uses threads, the multiprocessing module uses processes.     
2. threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. (Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. This is what the global interpreter lock is for.)         
3. Spawning processes is a bit slower than spawning threads. Once they are running, there is not much difference.       

<strong> Multiprocessing </strong>       
Pros    
Separate memory space   
Code is usually straightforward   
Takes advantage of multiple CPUs & cores    
Avoids GIL limitations for cPython    
Eliminates most needs for synchronization primitives unless if you use shared memory (instead, it's more of a communication model for IPC)    
Child processes are interruptible/killable    
Python multiprocessing module includes useful abstractions with an interface much like threading.Thread    
A must with cPython for CPU-bound processing    
   
Cons    
IPC a little more complicated with more overhead (communication model vs. shared memory/objects)    
Larger memory footprint    
   
     
<strong> Threading </strong>       
Pros   
Lightweight - low memory footprint   
Shared memory - makes access to state from another context easier   
Allows you to easily make responsive UIs    
cPython C extension modules that properly release the GIL will run in parallel    
Great option for I/O-bound applications    
  
Cons   
cPython - subject to the GIL   
Not interruptible/killable    
If not following a command queue/message pump model (using the Queue module), then manual use of synchronization primitives become a necessity (decisions are needed for the granularity of locking)    
Code is usually harder to understand and to get right - the potential for race conditions increases dramatically    








