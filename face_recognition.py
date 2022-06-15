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


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        #1st image
        img_top=Image.open(r"college_images\face_detector1.jpg")
        img_top=img_top.resize((650,700), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        #2st image
        img_bottom=Image.open(r"college_images\facial_recognition-large.jpg")
        img_bottom=img_bottom.resize((950,700), Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        #button
        b1_1=Button(f_lbl, text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=370, y=620, width=200, height=40)



    #=================attendance===================xuất file csv
    def mark_attendance(self,r,n,d):
        with open("attend.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and (d not in name_list)  ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Preset")


    #=========face recognition=====Hàm này có chức năng so sánh hình ảnh khuôn mặt đầu vào với tất cả các đặc trưng khuôn mặt từ file xml với mục đích tìm ra người dùng phù hợp với khuôn mặt đó. Sau đó tìm ra thông tin sinh viên trong cơ sở dữ liệu dựa trên msv tìm được

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):      #(image input, phát hiện khuôn mặt,thu nhỏ ảnh,số lần tối thiểu, màu sắc , nội dung, nhận dạng khuôn mặt)
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                            #chuyển thành màu xám
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)   #phát hiện khuôn mặt
            #phát hiện khuôn mặt trên camera
            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x + w, y + h),(0,255,0),2)  #tạo 1 hình chữ nhật màu xanh lá, độ dày đường viền là 2
                id, predict=clf.predict(gray_image[y: y+h, x: x+w])   #Dự đoán id của người dùng (predict ==>trả về độ chính xác(sai số) khi so sánh với file .xml)
                # print(id)
                # print(predict) # càng nhỏ thì càng nhận diện được  Khoảng tin cậy nhỏ hơn : Ước tính chính xác hơn.Khoảng tin cậy lớn hơn : Ước tính kém chính xác hơn
                confidence=int((100*(1-predict/300)))   #300 là kích thước của mẫu (kích thước mẫu càng lớn thì càng dễ nhận diện)

                conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
                my_cursor = conn.cursor()


                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)


                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                # my_cursor.execute("select Student_id from student where Student_id="+str(id))
                # i=my_cursor.fetchone()
                # i="+".join(i)



                if confidence > 80:
                    #(image input,nội dung chèn,tọa độ text,font chữ, kích cỡ, màu chữ,độ dày)
                    # cv2.putText(img, f"O.N:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Student_ID:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Deparment:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(r,n,d)


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

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #phát hiện khuôn mặt
        clf=cv2.face.LBPHFaceRecognizer_create()                                   #công cụ nhận dạng khuôn mặt
        clf.read("classifier.xml")                                                 #đọc file xml

        video_cap=cv2.VideoCapture(0)

        while True:
            ret, img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if (cv2.waitKey(1) == 13):
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()