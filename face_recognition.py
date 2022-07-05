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
listdata=[]
mylist = []


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        #1st image
        img_top=Image.open(r"college_images\face_detector1.jpg")
        img_top=img_top.resize((650,710), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=710)

        #2st image
        img_bottom=Image.open(r"college_images\facial_recognition-large.jpg")
        img_bottom=img_bottom.resize((950,710), Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=710)

        #button
        b1_1=Button(f_lbl, text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=370, y=620, width=200, height=40)



    def attend_absent_attendance(self,i, n, d):
        global namee
        with open("attend.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []

            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((i not in name_list) ):
                listdata.append(i)
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},YES")
                mystring = ",".join(listdata)

                conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Id, Name, Dep FROM studentinfo WHERE Id NOT IN (" + mystring + ")")
                namee = my_cursor.fetchall()

        with open('absent.csv', 'w', newline="\n") as p:
            if 'namee' in globals():
                for idd, naa, dee in namee:
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
                    p.writelines(f"\n{idd},{naa},{dee},{dtString},{d1},NO")


    #=================attendance===================
    # def mark_attendance(self,i,n,d):
    #     with open("attend.csv","r+",newline="\n") as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))
    #             name_list.append(entry[0])
    #
    #         if((i not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{n},{d},{dtString},{d1},YES")




    #=========face recognition====

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x + w, y + h),(0,255,0),2)
                id, predict=clf.predict(gray_image[y: y+h, x: x+w])
                confidence=int((100*(1-predict/300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
                my_cursor = conn.cursor()


                my_cursor.execute("select Name from studentinfo where Stt_s="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)


                my_cursor.execute("select Id from studentinfo where Stt_s="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Dep from studentinfo where Stt_s="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                # my_cursor.execute("select Stt_s from studentinfo where Stt_s="+str(id))
                # r=my_cursor.fetchone()
                # r="+".join(r)



                if confidence > 80:
                    # cv2.putText(img, f"O.N:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Student_ID:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Deparment:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.attend_absent_attendance(i,n,d)

                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img,"Unknow Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                confidence = " {0}%".format(round(confidence))
                cv2.putText(img, str(confidence), (x + 5, y + h - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)

                coord=[x,y,w,y]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,25,255),"Face", clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        count_id = 0
        while True:
            count_id+=1
            ret, img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            img=cv2.resize(img,(1300,790))
            cv2.imshow("Welcome To Face Recognition",img)

            if (cv2.waitKey(1) == 13) or (count_id == 100):
                break

        file1 = open("attend.csv", "a")
        file2 = open("absent.csv", "r")
        for line in file2:
            file1.write(line)

        file1.close()
        file2.close()
        video_cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()