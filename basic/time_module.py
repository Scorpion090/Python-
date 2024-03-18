# This is program for good morning with time module - 

import time
current_time = time.localtime().tm_hour
if(5<=current_time<=12):
    print("Good morning !")
elif(12<current_time<=18):
    print("Good afternoon!")
else:
    print("Good evening!")
    
# One other way to do this - 
import  time
timestamp = time.strftime("%H-%M-%S")
print(timestamp)

hour = int(time.strftime("%H"))
if(hour>0 and hour<12):
    print("Good morning")
elif(hour>12 and hour<18):
    print("Good afternoon")
else:
    print("Good evening")
