from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1020x540+0+0")
        self.root.title("thông tin sinh viên")


        title_lbl=Label(self.root,text="Thông Tin Sinh Viên Báo Cáo Tốt Nghiệp Khóa 19",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1020, height=45)
        #bg-img
        img_top=Image.open(r"college_images\laptopmy.jpeg")
        img_top=img_top.resize((1020,540), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1020, height=540)

        #admin1-img
        img_ad1=Image.open(r"college_images\ly7.jpg")
        img_ad1=img_ad1.resize((200,300), Image.ANTIALIAS)
        self.photoimg_ad1=ImageTk.PhotoImage(img_ad1)

        f_lbl=Label(self.root,image=self.photoimg_ad1)
        f_lbl.place(x=44, y=110, width=200, height=300)

        dev_label=Label(text="HUỲNH HỮU LÝ\n0308191044\nCD DTTT19MT", font=("times new roman",10,"bold"),bg="white",fg="blue")
        dev_label.place(x=44, y=410,width=200, height=55)

      #admin2-img
        img_ad2=Image.open(r"college_images\adminer.png")
        img_ad2=img_ad2.resize((200,300), Image.ANTIALIAS)
        self.photoimg_ad2=ImageTk.PhotoImage(img_ad2)

        f_lbl=Label(self.root,image=self.photoimg_ad2)
        f_lbl.place(x=288, y=60, width=200, height=300)

        dev_label=Label(text="BÙI MINH THIÊN\n0308191073\nCD DTTT19MT", font=("times new roman",10,"bold"),bg="white",fg="blue")
        dev_label.place(x=288, y=360,width=200, height=55)

     #admin3-img
        img_ad3=Image.open(r"college_images\huy.jpg")
        img_ad3=img_ad3.resize((200,300), Image.ANTIALIAS)
        self.photoimg_ad3=ImageTk.PhotoImage(img_ad3)

        f_lbl=Label(self.root,image=self.photoimg_ad3)
        f_lbl.place(x=532, y=110, width=200, height=300)

        dev_label=Label(text="PHẠM HUỲNH NHẬT HUY\n0308191037\nCD DTTT19MT", font=("times new roman",10,"bold"),bg="white",fg="blue")
        dev_label.place(x=532, y=410,width=200, height=55)

     #admin4-img
        img_ad4=Image.open(r"college_images\tinh.jpg")
        img_ad4=img_ad4.resize((200,300), Image.ANTIALIAS)
        self.photoimg_ad4=ImageTk.PhotoImage(img_ad4)

        f_lbl=Label(self.root,image=self.photoimg_ad4)
        f_lbl.place(x=776, y=60, width=200, height=300)

        dev_label=Label(text="NGUYỄN HUỲNH TRUNG TÍNH\n0308191084\nCD DTTT19MT", font=("times new roman",10,"bold"),bg="white",fg="blue")
        dev_label.place(x=776, y=360,width=200, height=55)


        dev_label=Label(text="Trường Cao Đẳng Kỹ Thuật Cao Thắng", font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=0, y=490,width=1020, height=40)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()