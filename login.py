from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System
# from face_recognition_admin import Face_recognition_admin
import cv2

#
# def face_recognition_admin():
#     win=Tk()
#     app=Login_Window(win)
#     win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")          #tiêu đề cửa sổ
        self.root.geometry("1550x800+0+0")  #kích thước của cửa sổ


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\WallpaperPlay.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0, relwidth=1, relheight=1)

        frame=Frame(self.root,bg="DarkOrange")
        frame.place(x=610, y=170, width=340, height=450)

        img1=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="DarkOrange",borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="DarkOrange")
        get_str.place(x=95,y=110)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="DarkOrange")
        username.place(x=65, y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40, y=180, width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="DarkOrange")
        password.place(x=65, y=225)

        self.txtpass=ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=40, y=250, width=270)

        #==========Icon Images=================

        img2=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="DarkOrange",borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)


        img3=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="DarkOrange",borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        #LoginButton======
        btn_login=Button(frame,command=self.login,cursor="hand2",text="Login",font=("times new roman",15,"bold"),bd=3, relief=RIDGE,fg="white",bg="Chocolate",activeforeground="white",activebackground="Chocolate")
        btn_login.place(x=40, y=300, width=120, height=35)

        btn_login=Button(frame,command=self.face_id,cursor="hand2",text="Face_ID",font=("times new roman",15,"bold"),bd=3, relief=RIDGE,fg="white",bg="Chocolate",activeforeground="white",activebackground="Chocolate")
        btn_login.place(x=190, y=300, width=120, height=35)

        #registerButton==================
        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="DarkOrange",activeforeground="white",activebackground="DarkOrange")
        registerbtn.place(x=15, y=350, width=160)

        #forgetpassbtn
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="DarkOrange",activeforeground="white",activebackground="DarkOrange")
        registerbtn.place(x=10, y=370, width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def num1(self, ye):
        if ye == 1:
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_System(self.new_window)

    def num2(self, no):
        if no == 2:
            self.root.destroy()
    def face_id(self):
        def draw_boundray(img, classifier_admin, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier_admin.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y: y + h, x: x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",
                                                   database="systerm_admin")
                my_cursor = conn.cursor()

                my_cursor.execute("select Id from adminstrator where On_s=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select Name from adminstrator where On_s=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                if confidence > 80:
                    cv2.putText(img, f"Id:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.num1(1)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknow", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.num2(2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier_admin.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                face_cropped = img[y: y + h, x:x + w]
                return face_cropped

        video_cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, img = video_cap.read()
            if face_cropped(img) is not None:
                img_id += 1
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome To Face Recognition", img)

                if (cv2.waitKey(1) == 13 or (img_id == 1)):
                    time.sleep(3)
                    break

        video_cap.release()
        cv2.destroyAllWindows()

        # self.new_window = Toplevel(self.root)
        # self.app = Face_recognition_admin(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="thien":
            messagebox.showinfo("Success","Welcome to group one")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Thien@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(

                                                                            self.txtuser.get(),
                                                                            self.txtpass.get()
                                                                                ))
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Inavalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main > 0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #===========================reset password===================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error", "Select the security quetion",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Thien@123",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()



    #===================================forgot password windown==============
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error","Please Winter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Thien@123",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            values=(self.txtuser.get(),)
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            print(row)

            if row == None:
                messagebox.showerror("My Error", "Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Quetions", font=("times new roman", 15, "bold"),bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",cursor="hand2",command=self.reset_pass,font=("times new roman", 15, "bold"),fg="White",bg="blue")
                btn.place(x=140, y=290)





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #=====================Variables ===========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #==============bg image============
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\hackers2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


        #==============left image============
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\messages-LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)


        #===========main Frame======================
        frame=Frame(self.root,bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl=Label(frame, text="REGISTER HERE", font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20, y=20)

        #===========label and entry========================
        #==================row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50, y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50, y=130, width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370, y=130, width=250)

        #==================row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50, y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50, y=200, width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370, y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_contact.place(x=370, y=200, width=250)


        #==================row3
        security_Q=Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50, y=240)


        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place", "Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370, y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370, y=270, width=250)

        #==================row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)


        #==============checkbuton=======================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",15,"bold"))
        self.checkbtn.place(x=50, y=380)



        #====================buttons=======================
        img=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\register-now-button1.jpg")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10, y=420, width=200)


        img1=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\loginpng.png")
        img1=img1.resize((200,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330, y=420, width=200)

        #===================Function declaration=========================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm password must be same")
        elif self.var_check.get() ==0:
            messagebox.showerror("Error", "Please argee our terms ane condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Thien@123",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()



if __name__=="__main__":
    win=Tk()                #tạo cửa số mới
    app=Login_Window(win)   #chương trình chạy
    win.mainloop()          # mainloop () là một vòng lặp vô hạn dùng để hiển thị cửa sổ, đợi một sự kiện xảy ra và xử lý sự kiện miễn là cửa sổ chưa được đóng.

