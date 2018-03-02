#capturing a photo every five seconds

import os
import time
t=0
k=1
while(t<2):
    time.sleep(5)
    os.system("fswebcam -F 5 --fps 20 -r 1200x800 /home/pi/"+str(k)+"35.jpg,36.jpg")
    print("captured")
    t+=1
    k+=1
