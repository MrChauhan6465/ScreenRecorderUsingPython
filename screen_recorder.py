import cv2 
import pyautogui
from win32api import GetSystemMetrics
import numpy
import time

#for getting screen resolution
width  = GetSystemMetrics(0) 
height = GetSystemMetrics(1)
dim = (width,height)

#making video in xvid format 
f = cv2.VideoWriter_fourcc(*"XVID")

#saving video 

output = cv2.VideoWriter("test_video.mp4",f,30.0,dim)

#setting times
now_start_time = time.time()
duration = int(input("Enter the duration of video in seconds \n(note : add 4 sec more for more efficiency\n)"))

end_time = now_start_time+duration
while True:
    image = pyautogui.screenshot()
    frame1 = numpy.array(image)
    frame = cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break

output.release()

print("___Your video is recorded___")
print