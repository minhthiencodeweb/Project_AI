from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=45)
        #top-img
        img_top=Image.open(r"college_images\face_header_pc.jpg")
        img_top=img_top.resize((1530,325), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        #button
        b1_1=Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        #bot-img
        img_bottom=Image.open(r"college_images\train-dataset.jpg")
        img_bottom=img_bottom.resize((1530,325), Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)


    #=================lấy ảnh và địa chỉ ip trong thư viện data =======================chuyển đổi ảnh và id thành dạng numpy
    def train_classifier(self):
        data_dir=("data")                                                     #Sử dụng phương thức os.path.join () để nối các thành phần đường dẫn khác nhau
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]   # os.listdir ==>trả về danh sách các thư mục hoặc file có trong đường dẫn cung cấp
        #==> path = đường dẫn của ảnh
        faces=[]   #chứa px của hình ảnh
        ids=[]     #chưa id của hình ảnh dc train

        for image in path:
            img=Image.open(image).convert('L')                                #Gray scale image              #tải hình ảnh từ file và chuyển đổi hình ảnh sang màu trắng đen và xám
            imageNp=np.array(img,'uint8')                                     #tạo ra  ma trận các điểm ảnh
            id=int(os.path.split(image)[1].split('.')[1])                     #data\user.1.1.jpg ==> tách id từ tên file ảnh (data[0], user.1.1.jpg[1]) lấy id để ảnh hiển là nó thuộc id nào
            #khi chạy xong id 1 sẽ tiếp tục lấy id 2 ...

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)                                    #hiển thị tất cả các ảnh trong thư viện dạng numpy

            cv2.waitKey(1)==13
        ids=np.array(ids)                                                     #chuyển danh sách id thành dạng numpy
        #===========Train the classifier And save========
        clf=cv2.face.LBPHFaceRecognizer_create()                              #công cụ nhận dạng khuôn mặt
        clf.train(faces,ids)                                                  #dùng mảng ids và faces để traindata(gán ảnh đó với id)
        clf.write("classifier.xml")                                           #train và lưu vào thư mục xml (chứa đặt trưng khuôn mặt sao khi train)
        cv2.destroyAllWindows()
        # messagebox.showinfo("Result","Training datasets completed!!")






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()