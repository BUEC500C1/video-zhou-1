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




