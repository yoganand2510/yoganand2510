import os
import time
import tweepy	
consumer_key='vAyBa8mCJk0FUyrxFNDScL8Is'
consumer_secret='p0XgMgQv76hg0Jw43rD9UKdijZRaJTMfDSpRiFxXTFwRhVaOE6'
access_token='704591968068771840-4ryUusS3mbHXoYEq5BJ6Itami1FTPPZ'
access_token_secret='uWYdcZGODwy3ykCTlOMJEEvxQsG6UYF9FLtF3l1FjVRGy'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/user/desktop/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 800x600"+img
    os.system(cmd)
    print("captured")

    
    api.update_with_media(img, status='nice')
    print('wait for 5 sec for sefli')
    time.sleep(5)
    a+=1
    b+=1
    print("selfi mene leliya")
