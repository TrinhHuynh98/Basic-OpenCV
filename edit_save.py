# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import datetime
import os
import sys
def test():
        def select_image():
                # put image position in their channel
                global panelA, panelB, prevImg
                panelA = None
                panelB = None
                # allow for choice file to input
                # image
                path = filedialog.askopenfilename()
                # checking open file 
                if len(path) > 0:
                        # open orignal file and cover inmage to gray and detect
                        image = cv2.imread(path)
                        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        edged = cv2.Canny(gray, 100, 100)
                        prevImg = Image.fromarray(gray)
                        imgtk = ImageTk.PhotoImage(image=prevImg)
                        #lmain.imgtk = imgtk
                        #lmain.configure(image=imgtk)
                        
                        
                        # images in RGB order, so we need to swap the channels
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        
         
                        # convert the images to PIL format...
                        image = Image.fromarray(image)
                        edged = Image.fromarray(edged)
                        
                
                        # ...and then to ImageTk format
                        image = ImageTk.PhotoImage(image)
                        edged = ImageTk.PhotoImage(edged)
                        
                        
                        # if the panels are None, initialize them
                        if panelA is None or panelB is None:
                                # the first panel will store our original image
                                panelA = Label(image=image)
                                panelA.image = image
                                panelA.pack(side="left", padx=10, pady=10)
         
                                # while the second panel will store the edge map
                                panelB = Label(image=edged)
                                panelB.image = edged
                                panelB.pack(side="right", padx=10, pady=10)
         
                        # otherwise, update the image panels
                        else:
                                # update the pannels
                                panelA.configure(image=image)
                                panelB.configure(image=edged)
                                panelA.image = image
                                panelB.image = edged
                                
                
                
                                
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
            
            
            #mainWindow.quit()
                        
        # initialize the window toolkit along with the two image panels
        root = Tk()
        
         
        # create a button, then when pressed, will trigger a file chooser
        # dialog and allow the user to select an input image; then add the
        # button the GUI

        btn1 = Button(root, text="Save Image", command=saveAndExit)
        btn = Button(root, text="Select an image", command=select_image)
        btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
        btn1.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

        # kick off the GUI
        root.mainloop()
                
		
