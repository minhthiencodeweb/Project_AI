# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# from time import strftime
# from datetime import datetime
# import cv2
# import os
# import numpy as np
# import time
# from main import Face_Recognition_System
# # from login import Login_Window
#
#
#
#
# #face ID login
# class Face_recognition_admin:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("face Recognition System")
#
#         #===============variables===============
#         self.var_id=StringVar()
#         self.var_name=StringVar()
#
#         title_lbl=Label(self.root,text="ADMINISTRATION STUDENT",font=("times new roman",35,"bold"),bg="white",fg="green")
#         title_lbl.place(x=0,y=0,width=1530, height=45)
#
#
#         #2st image
#         img_bottom=Image.open(r"college_images\admin_btn.jpg")
#         img_bottom=img_bottom.resize((1600,700), Image.ANTIALIAS)
#         self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
#
#         f_lbl=Label(self.root,image=self.photoimg_bottom)
#         f_lbl.place(x=0, y=55, width=1600, height=700)
#
#         #button
#         b1_1=Button(f_lbl, text="Face Admin",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="snow",fg="black")
#         b1_1.place(x=650, y=500, width=200, height=40)
#
#
#     def num1(self,ye):
#         if ye == 1:
#             self.new_window = Toplevel(self.root)
#             self.app = Face_Recognition_System(self.new_window)
#
#     def num2(self,no):
#         if no == 2:
#             self.root.destroy()
#
#
#     #=========face recognition============
#     #Id trong database là varchar(45)
#     def face_recog(self):
#         def draw_boundray(img,classifier_admin,scaleFactor,minNeighbors,color,text,clf):
#             gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features=classifier_admin.detectMultiScale(gray_image,scaleFactor,minNeighbors)
#
#             coord=[]
#
#             for(x,y,w,h) in features:
#                 cv2.rectangle(img,(x,y), (x + w, y + h),(0,255,0),2)
#                 id, predict=clf.predict(gray_image[y: y+h, x: x+w])
#                 confidence=int((100*(1-predict/300)))
#
#                 conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="systerm_admin")
#                 my_cursor = conn.cursor()
#
#
#                 my_cursor.execute("select Id from adminstrator where On_s="+str(id))
#                 i=my_cursor.fetchone()
#                 i="+".join(i)
#
#
#                 my_cursor.execute("select Name from adminstrator where On_s="+str(id))
#                 n=my_cursor.fetchone()
#                 n="+".join(n)
#
#
#                 if confidence > 80:
#                     cv2.putText(img, f"Id:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
#                     cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
#                     # self.mark_attendance(i,n)
#                     self.num1(1)
#                 else:
#                     cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 2)
#                     cv2.putText(img,"Unknow", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
#                     self.num2(2)
#
#
#                 coord=[x,y,w,h]
#             return coord
#         def recognize(img, clf, faceCascade):
#             coord = draw_boundray(img, faceCascade, 1.1, 10, (255,255,255),"Face", clf)
#             return img
#
#
#
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier_admin.xml")
#
#         def face_cropped(img):
#             gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             faces = faceCascade.detectMultiScale(gray, 1.3,5)
#
#
#             for (x, y, w, h) in faces:
#                 face_cropped = img[y: y + h, x:x + w]
#                 return face_cropped
#
#
#         video_cap=cv2.VideoCapture(0)
#         img_id=0
#         while True:
#             ret, img=video_cap.read()
#             if face_cropped(img) is not None:
#                 img_id+=1
#                 img=recognize(img, clf, faceCascade)
#                 cv2.imshow("Welcome To Face Recognition",img)
#
#                 if (cv2.waitKey(1)==13 or (img_id == 1)):
#                     time.sleep(3)
#                     break
#
#         video_cap.release()
#         cv2.destroyAllWindows()
#
#
#
#
# if __name__=="__main__":
#     root=Tk()
#     obj=Face_recognition_admin(root)
#     root.mainloop()
#
#
#
