import tkinter as tk
import os
import cv2
import sys
from PIL import Image, ImageTk
import numpy
import datetime
from tkinter import Button
global fileName, cancel
fileName = os.environ['ALLUSERSPROFILE'] + "\WebcamCap.txt"
cancel = False




def test():
    def prompt_ok(event = 0):
        global cancel
        cancel = True

        button.place_forget()
        
        button1.place(anchor=tk.CENTER, relx=0.2, rely=0.9, width=150, height=50)
        button2.place(anchor=tk.CENTER, relx=0.8, rely=0.9, width=150, height=50)
        button1.focus()

    def saveAndExit(event = 0, output_path = "./"):
        global prevImg
        prevImg.current_image = None
        prevImg.output_path = output_path
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        p = os.path.join(prevImg.output_path, filename)
        if prevImg is not None:
            prevImg.save(p, "JPEG")
       # prevImg.current_image.save(p, "JPEG")
        
        
        mainWindow.quit()


    def resume(event = 0):
        global button1, button2, button, lmain, cancel

        cancel = False

        button1.place_forget()
        button2.place_forget()

        mainWindow.bind('<Return>', prompt_ok)
        button.place(bordermode=tk.INSIDE, relx=0.5, rely=0.9, anchor=tk.CENTER, width=300, height=50)
        lmain.after(10, show_frame)


    def CamCheck(event=0):
        global camIndex, cap, fileName

        del(cap)
        cap = cv2.VideoCapture(camIndex)

        #try to get a frame, if it returns nothing
        success, frame = cap.read()
        if not success:
            camIndex = 0
            del(cap)
            cap = cv2.VideoCapture(camIndex)

        f = open(fileName, 'w')
        f.write(str(camIndex))
        f.close()

    try:
        f = open(fileName, 'r')
        camIndex = int(f.readline())
    except:
        camIndex = 0

    cap = cv2.VideoCapture(camIndex)
    capWidth = cap.get(3)
    capHeight = cap.get(4)

    success, frame = cap.read()

    global button, button1, button2, mainWindow, lmain
    mainWindow = tk.Tk(screenName="Camera Capture")
    mainWindow.resizable(width=False, height=False)
    mainWindow.bind('<Escape>', lambda e: mainWindow.quit())
    lmain = tk.Label(mainWindow, compound=tk.CENTER, anchor=tk.CENTER, relief=tk.RAISED)
    
    lmain.pack()
    button1 = tk.Button(mainWindow, text="Save Image!", command=saveAndExit)
    button2 = tk.Button(mainWindow, text="Try Again", command=resume)
    button = tk.Button(mainWindow, text="Capture", command=prompt_ok)
    button.place(bordermode=tk.INSIDE, relx=0.5, rely=0.9, anchor=tk.CENTER, width=300, height=50)
    button.focus()

    def show_frame():
        global cancel, prevImg, button

        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        prevImg = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=prevImg)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        if not cancel:
            lmain.after(10, show_frame)

    show_frame()
    mainWindow.mainloop()
