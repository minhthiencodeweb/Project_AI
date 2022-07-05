from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train_admin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA ADMIN",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=45)
        #bg-img
        img_top=Image.open(r"college_images\huong-dan-quan-ly.png")
        img_top=img_top.resize((1530,750), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1530, height=750)

        #button
        b1_1=Button(self.root, text="TRAIN",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="green")
        b1_1.place(x=670, y=600, width=200, height=40)


    def train_classifier(self):
        data_dir=("datadmin")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training-admin",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #===========Train the classifier And save========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier_admin.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!", parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Train_admin(root)
    root.mainloop()