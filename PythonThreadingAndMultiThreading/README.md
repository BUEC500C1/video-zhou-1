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
