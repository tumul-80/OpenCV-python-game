'''
This code is of a 'game' which allows the user to change the position of a circle, 
which is superimposed over a video. It was created for the purpose of an experiment
where the particiapnt's reaction to changing active speaker were to be determined.

Created by: Tumul Kumar. 2021. 
'''

import cv2 as cv #import the OpenCV library
import numpy as np #Import Numpy Library
import socket  # socket creation for Telnet
from datetime import datetime
from telnetlib import Telnet #telnet client
from ffpyplayer.player import MediaPlayer #ffpyplayer for playing audio

current_date_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
HOST = '127.0.0.1'  # The remote host
PORT = 4212  # The same port as used by the server
TCP_PORT = 9999  # port used to connect with the server file

def send_data(message, s, output): #to send the data to the TCP_server
    s.sendall(message.encode())
    data = s.recv(1024)
    output.write('\n'+ current_date_time+' '+message+ '\n')
    return data
#to create the circle
def circle(frame, left): 
    if left:
        cv.circle(frame,(450,250),20,(255,255,255),50) 
    if not left:
        cv.circle(frame,(1400,250),20,(255,255,255),50)
#to create the actual video output of the game
def video():
    cap1 = cv.VideoCapture('P1.mp4') # the video that we want
    player = MediaPlayer('P1.mp4')
    circle_is_left = True
    if (cap1.isOpened()== False):
        print("Error opening video 1")  
    while (cap1.isOpened()):
        ret,frame = cap1.read() #capture frame-by-frame video
        audio_frame,val=player.get_frame() # capture frame-by-frame audio
        if ret== True:
            key_pressed = cv.waitKey(1)
            if key_pressed == ord(' '): #pressing space bar ends the video
                with open('out.txt', 'a') as output:
                    send_data('video 1 is changed',s,output)
                break
            elif key_pressed == 2: #left key pressed changes circle to lett
                circle_is_left = True
                with open('out.txt', 'a') as output:
                    send_data('left',s,output)
            elif key_pressed == 3: # right key pressed changes circle to right
                circle_is_left = False
                with open('out.txt', 'a') as output:
                    send_data('Right ',s,output)
            circle(frame, circle_is_left) #display the circle at all times
            cv.imshow('cap1',frame) #display resulting frame 
            if val != 'eof' and audio_frame is not None:
                img,t = audio_frame
    cap1.release()
    cv.destroyAllWindows()
 
    cap2 = cv.VideoCapture('P2.mov') # the video that we want
    player2 = MediaPlayer('P2.mov')
    circle_is_left = True
    if (cap2.isOpened()== False):
        print("Error opening video 2")  
    while (cap2.isOpened()):
        ret,frame = cap2.read() #capture frame-by-frame video
        audio_frame,val=player2.get_frame() # capture frame-by-frame audio
        if ret== True:
            key_pressed = cv.waitKey(1)
            if key_pressed == ord(' '): #pressing space bar ends the video
                with open('out.txt', 'a') as output:
                    send_data('video 1 is changed',s,output)
                break
            elif key_pressed == 2: #left key pressed changes circle to lett
                circle_is_left = True
                with open('out.txt', 'a') as output:
                    send_data('left',s,output)
            elif key_pressed == 3: # right key pressed changes circle to right
                circle_is_left = False
                with open('out.txt', 'a') as output:
                    send_data('Right ',s,output)
            circle(frame, circle_is_left) #display the circle at all times
            cv.imshow('cap2',frame) #display resulting frame 
            if val != 'eof' and audio_frame is not None:
                img,t = audio_frame
    cap2.release()
    cv.destroyAllWindows()

def main():
    print("Game1.py is connected to TCP server")
    video()
    
if __name__=='__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, TCP_PORT))
    main()
