Python process and subprocess     
https://docs.python.org/3/library/subprocess.html      

<strong> The subprocess module </strong>       
allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.       

1. The run() function     
was added in Python 3.5; if you need to retain compatibility with older versions, see the Older high-level API section.     
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)      

2. subprocess.CompletedProcess    
The return value from run(), representing a process that has finished.     

3. subprocess.DEVNULL   

4. subprocess.PIPE   

5. subprocess.STDOUT    

6. exception subprocess.CalledProcessError     


The underlying process creation and management in this module is handled by the <strong>Popen class </strong>. It offers a lot of flexibility so that developers are able to handle the less common cases not covered by the convenience functions.         
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None, text=None)        

<strong> Exceptions </strong>    

<strong> Security Considerations </strong>     

<strong> Popen Objects </strong>   
Instances of the Popen class have bunch of methods.     

<strong> Windows Popen Helpers </strong>    

<strong> Replacing Older Functions with the subprocess Module </strong>   




