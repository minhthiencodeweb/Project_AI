from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import time
from main import Face_Recognition_System
# from login import Login_Window


# def main():
#     win=Tk()
#     app=Face_recognition_admin(win)
#     win.mainloop()

# def login():
#     win=Tk()
#     app=Face_recognition_admin(win)
#     win.mainloop()
lis=[]

#face ID login
class Face_recognition_admin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #===============variables===============
        self.var_id=StringVar()
        self.var_name=StringVar()

        title_lbl=Label(self.root,text="ADMINISTRATION STUDENT",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530, height=45)


        #2st image
        img_bottom=Image.open(r"college_images\admin_btn.jpg")
        img_bottom=img_bottom.resize((1600,700), Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0, y=55, width=1600, height=700)

        #button
        b1_1=Button(f_lbl, text="Face Admin",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="snow",fg="black")
        b1_1.place(x=650, y=500, width=200, height=40)


    def num1(self,ye):
        count=0
        while True:
            count+=1
            if ye ==1:
                if count ==100:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                    break




        # if ye == 1:
        #     self.new_window = Toplevel(self.root)
        #     self.app = Face_Recognition_System(self.new_window)

    def num2(self,no):
        if no == 2:
            self.root.destroy()


    #=================attendance===================
    # def mark_attendance(self,i,n):
    #     with open("attend_admin.csv","r+",newline="\n") as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))
    #             name_list.append(entry[0])
    #         if((i not in name_list) and (n not in name_list) ):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{n},{dtString},{d1},Preset")


    #=========face recognition============
    #Id trong database là varchar(45)
    def face_recog(self):
        def draw_boundray(img,classifier_admin,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier_admin.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x + w, y + h),(0,255,0),3)
                id, predict=clf.predict(gray_image[y: y+h, x: x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="systerm_admin")
                my_cursor = conn.cursor()


                my_cursor.execute("select Id from adminstrator where On_s="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                my_cursor.execute("select Name from adminstrator where On_s="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                if confidence > 80:
                    cv2.putText(img, f"Id:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # self.mark_attendance(i,n)
                    lis.append(1)


                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknow", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.num2(2)


                coord=[x,y,w,h]
            return coord
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,255,255),"Face", clf)
            return img



        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier_admin.xml")                    #khuôn mặt trên máy

        video_cap=cv2.VideoCapture(0)

        img_id=0
        while True:
            ret, img=video_cap.read()
            img_id+=1
            img=recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if (cv2.waitKey(1)==13 or (img_id == 50)):
                if lis[0]==1:
                    self.num1(1)
                break

        video_cap.release()
        cv2.destroyAllWindows()




if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_admin(root)
    root.mainloop()



