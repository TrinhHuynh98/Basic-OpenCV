#importing modules required
from tkinter import *
import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
import edit_save
import load_video
import capture


global root
root=tk.Tk() 
global last_frame                                      #creating global variable
last_frame = np.zeros((480, 640, 3), dtype=np.uint8)
global cap
cap = cv2.VideoCapture(0)
global lmain
lmain = tk.Label(root)
#lmain1 = tk.Label(root)

def show_vid():
    #creating a function
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#    lmain1.configure(image=img)
    cv2.imshow('Face&Eyes Detection',img)
 
    if not cap.isOpened():                             #checks for the opening of camera
        print("cant open the camera")
    flag, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if flag is None:
        print ("Major error!") 
    elif flag:
        global last_frame
        last_frame = frame.copy()

    pic = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)     #we can change the display color of the frame gray,black&white here
    img = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(50, show_vid)

    
def multi():
    root.destroy()
    capture.test()
def multi1():
    root.destroy()
    cv2.destroyAllWindows()
    load_video.test()
if __name__ == '__main__':
#   root=tk.Tk()                                     #assigning root variable for Tkinter as tk
#    lmain = tk.Label(master=root)
#    lmain.grid(column=0, rowspan=4, padx=5, pady=5)
    lmain.pack()
#    lmain1.pack()
    root.title("OpenCV Application")#you can give any title
    frame = Frame(root, relief=RAISED, borderwidth=10)
    frame.pack(fill=BOTH, expand=True)
#    self.pack(fill=BOTH, expand=True)
#    label = tk.Label(frame, command=live_video.show_vid())
#    label.pack(fill=BOTH, expand=True)
     
    show_vid() 
    capButton = Button(root, text="Cap",command=multi, bg='silver')
    capButton.pack(side=LEFT, ipadx=50, ipady=8, padx=5, pady=5)
    loadButton = Button(root, text="Load", command=multi1, bg='silver')
    loadButton.pack(side=LEFT, ipadx=50, ipady=8, padx=5, pady=5)
    exitButton = Button(root, text="Exit", command=root.destroy, bg='silver')
    exitButton.pack(side=RIGHT, ipadx=50, ipady=8, padx=5, pady=5)
    editButton = Button(root, text="Edit", command=edit_save.test, bg='silver')
    editButton.pack(side=RIGHT, ipadx=50, ipady=8, padx=5, pady=5)
    
    
    root.mainloop()                                  #keeps the application in an infinite loop so it works continuosly
    cap.release()
    cv2.destroyAllWindows
