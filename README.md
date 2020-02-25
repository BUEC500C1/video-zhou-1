# video-zhou-1    
video-zhou-1 created by GitHub Classroom         
<strong> Collect contents of tweets from targeted twitter user, convert the contents to images and videos.       
My program provides 2 different versions of video: normal one and better one with better quality. </strong>    
    
<strong>Technology used in this repo:</strong>       
Twitter tweepy API   
![tweepy](/imgs/tweepy.png)    

ffmpeg-python     
![ffmpeg](/imgs/ffmpeg-python.PNG)   

Own-built queue    
![queue](https://github.com/BUEC500C1/video-zhou-1/blob/master/imgs/queue.png)   


# What did I do?       
<strong>Task 0 - part 1:</strong>        
Study [PythonProcessAndSubprocess](https://github.com/BUEC500C1/video-zhou-1/tree/master/PythonProcessAndSubprocess)      
Study [PythonThreadingAndMultiThreading](https://github.com/BUEC500C1/video-zhou-1/tree/master/PythonThreadingAndMultiThreading)        
Study [PythonThreadsVSProcesses](https://github.com/BUEC500C1/video-zhou-1/tree/master/PythonThreadsVSProcesses)      
Run and test the code provided in https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python and compare processes and threads        
[ThreadsVSProcesses.py](https://github.com/BUEC500C1/video-zhou-1/tree/master/Task0)           

<strong>Task 1: </strong>      
Play with FFmpeg to test for coverting image to video.      
[encodeVideoFiles.py and another markdown file for encoding video commands.](https://github.com/BUEC500C1/video-zhou-1/tree/master/Task1)        

<strong>Task 2: </strong>      
Step 1:   
Develop a queue system that can exercise your requirements with stub functions.    
Step 2:   
Develop the twitter functionality with an API   
Step 3:   
Integrate them      
Task 2 can be [viewed here.](https://github.com/BUEC500C1/video-zhou-1/tree/master/Task2)    
   

# Answers to the hw questions    
For re-encoding video files:   
1. Estimate the processing power need to execute such operations on computer      
Each of them costs around ~200% processing power on CPU.   
2. Estimate the maximum number of such operations that can run on system      
For my laptop, I have 4 cores, 8 logical processors in my CPU. So in order to lose no quality or speed, the maximum number of such operation should be 4 on the system.   

For Task 2 questions:    
1. How many API calls you can handle simultaneously and why?    
Currently I have 1 worker so I can only handle with 1 API call at this time. However, it is easy to implement more worker in my program and because I have 8 logical processors, I can build 7 more workers in order to handle with 8 API calls simultaneously.      

2. For example, run different API calls at the same time?      
Yes.    

3. Split the processing of an API into multiple threads?     
I splited them into 4 threads for my worker.    

# Setup     
Clone my current repo:     
https://github.com/BUEC500C1/video-zhou-1.git      
OR    
Use below command:    
```
git clone https://github.com/BUEC500C1/video-zhou-1.git   
```
   
Go to [Task2](https://github.com/BUEC500C1/video-zhou-1/tree/master/Task2) folder.       
Please go to keys file, to add in your own Tweepy API keys in below format:   
```
[auth]
consumer_key = ****
consumer_secret = ****
access_token = ****
access_secret = ****
```

To run the whole program, next please run the Python file sysQueue.py:    
```
python sysQueue.py
```
     
It will automatically show you images of default twitter users' tweets and 2 verisions of videos of these images.     
If you would like to build videos for different twitter accounts, please go to sysQueue.py file and modify the contents of below line:   
```
keyNames = ['BU_ece', 'BU_CCD', 'BU_CAS', 'BU_Tweets', 'realDonaldTrump', 'BarackObama', 'RealTonyStark', '_Spiderman', 'amazon', 'Google', 'Microsoft', 'LinkedIn']
```   
## Test   
For pytest, I tested results for whether required videos exist or not by comparing the names; All tests passed.    

For testing for whether keys file exist or not, whether keys file is empty or not, whether keys file has main and sub title or not; if answer for any of them is no, we need to call <b>get_oldJson</b> function. This function is in tweepyInfo.py file.       

<b>Caution: </b> In order to use my get_oldJson function successfully, you need to have json file for the desired twitter account first. I had already put in default 10 twitter user's tweets in jsonFolder; therefore, if keys file fail, we can get information from previous json file.    
Moreover, every time out program successfully with right keys file, json files for those twitter account will get updated, too.    


## Processing tracking UI   
For the process tracking UI, I have below code to take care of:    
```
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
```


# Achievement    
<b>Output images will be like below:</b>        
![img](/imgs/outputImages.PNG)   
      
         
          
<strong>Output videos will be like below:</strong>       
![vdio](/imgs/outputVideo.PNG)   

    
<strong> User Interface for tracking process </strong>    
![UI1](/imgs/UI1.PNG)     
![UI2](/imgs/UI2.PNG)    


