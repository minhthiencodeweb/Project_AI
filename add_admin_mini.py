from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from train_admin import Train_admin


class adminstator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1020x540+0+0")
        self.root.title("face Recognition System")

        #===============variables===============
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_phone=StringVar()
        self.var_gmail=StringVar()
        self.var_addr=StringVar()
        self.var_on=StringVar()
        self.var_gen=StringVar()


        #first image
        img=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\Cap.PNG")
        img=img.resize((1020,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1020, height=100)


        #bg-image
        img3=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\background-main.jpg")
        img3=img3.resize((1020,540), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1020, height=540)

        title_lbl=Label(bg_img,text="ADMIN MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1020, height=35)

        #mainframe
        main_frame=Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=970, height=380)

        # left lable frame
        left_inside_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Admin Details", font=("times new roman",12,"bold"))
        left_inside_frame.place(x=10, y=10, width=320, height= 360)

        #STT
        nameLabel=Label(left_inside_frame,text="STT:",bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=0,column=0)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_on,width=20,font="comicsansns 11 bold")
        atten_name.grid(row=0,column=1,pady=8)


        #Student id
        attendance_label=Label(left_inside_frame,text="ID Quản Trị:", font="comicsansns 11 bold",bg="white")
        attendance_label.grid(row=1,column=0)

        attendance_entry=ttk.Entry(left_inside_frame,textvariable=self.var_id,width=20,font="comicsansns 11 bold")
        attendance_entry.grid(row=1,column=1,padx=8,pady=10)

        #Name Admin
        rollLabel=Label(left_inside_frame,text="Tên Quản Trị:",bg="white", font="comicsansns 11 bold")
        rollLabel.grid(row=2,column=0)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_name,width=20,font="comicsansns 11 bold")
        atten_roll.grid(row=2,column=1,pady=8)

        #Gmail
        depLabel=Label(left_inside_frame,text="Gmail:",bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=3,column=0)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_gmail,width=20,font="comicsansns 11 bold")
        atten_dep.grid(row=3,column=1,pady=8)

        #Address
        timeLabel=Label(left_inside_frame,text="Địa Chỉ:",bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=4,column=0)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_addr,width=20,font="comicsansns 11 bold")
        atten_time.grid(row=4,column=1,pady=8)

        #Phone
        dateLabel=Label(left_inside_frame,text="Điện Thoại",bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=5,column=0)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_phone,width=20,font="comicsansns 11 bold")
        atten_date.grid(row=5,column=1,pady=8)


        #Gender
        attendanceLabel=Label(left_inside_frame,text="Giới Tính:",bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=6,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_gen,width=18,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Male","Female","Other")
        self.atten_status.grid(row=6,column=1,pady=8)
        self.atten_status.current(0)


        #buttons frame
        btn_frame=Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=316, height=38)

        save_btn=Button(btn_frame,text="Add Admin",command=self.add_data, width=15,font=("times new roman", 13, "bold"),bg="blue",fg="white" )
        save_btn.grid(row=0, column=0)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=1)



        #==========Serach System================
        Search_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Search", font=("times new roman",12,"bold"))
        Search_frame.place(x=340, y=10, width=625, height=360)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 12, "bold"),fg="blue",bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)



        #button frame1
        btn_frame1=Frame(Search_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=301, width=630, height=35)

        update_btn = Button(btn_frame1, text="Update",command=self.update_data, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame1, text="Delete ",command=self.delete_data, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample ",command=self.generate_dataset, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=3)

        update_photo_btn = Button(btn_frame1, text="Train Data",command=self.totrain,width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=4)



        #search-------
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=("times new roman",12,"bold"),state="readonly",width=12)
        search_combo["values"]=("Select","Id","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(Search_frame,textvariable=self.var_search, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # ------------
        search_btn = Button(Search_frame, text="Search",command=self.search_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, text="Show All",command=self.fetch_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4,padx=4)


        #===============table frame================
        table_frame=Frame(Search_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=0, y=50, width=620, height=245)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("on","id","name","gen","phone","gmail","addr"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("id",text="ID_Quản Trị")
        self.student_table.heading("name",text="Tên Quản Trị")
        self.student_table.heading("gen", text="Giới Tính")
        self.student_table.heading("phone", text="Số Điện Thoại")
        self.student_table.heading("gmail", text="Gmail")
        self.student_table.heading("addr", text="Địa Chỉ")
        self.student_table.heading("on", text="STT")
        self.student_table["show"]="headings"

        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("gen", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("gmail", width=100)
        self.student_table.column("addr", width=100)
        self.student_table.column("on", width=50)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def totrain(self):
        self.new_window1 = Toplevel(self.root)
        self.app = Train_admin(self.new_window1)


    def add_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_on.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Thien@123",database="systerm_admin")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into adminstrator values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_on.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_gen.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_gmail.get(),
                                                                                                                self.var_addr.get()
                                                                                                                                    ))   #ảnh hưởng đên thứ tự yêu cầu sx đúng
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #=================fetch data===============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="systerm_admin")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from adminstrator")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    #======get cursor===========
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_on.set(data[0]),
        self.var_id.set(data[1]),
        self.var_name.set(data[2]),
        self.var_gen.set(data[3]),
        self.var_phone.set(data[4]),
        self.var_gmail.set(data[5]),
        self.var_addr.set(data[6])


    #========update fuction======
    def update_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_on.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Upadate", "Do you want to admin this student details",parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="systerm_admin")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update adminstrator set Id=%s,Name=%s,Gen=%s,Phone=%s,Gmail=%s,Addr=%s where On_s=%s ",(   #On_s ---- _ ------ trong mysql
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_gen.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_gmail.get(),
                                                                                                                self.var_addr.get(),
                                                                                                                self.var_on.get()
                                                                                                                                ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student admin successfully admin completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    #============delete function==========
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123", database="systerm_admin")
                    my_cursor = conn.cursor()
                    sql="delete from adminstrator where Id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


    #====reset =============
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_phone.set("")
        self.var_gmail.set("")
        self.var_addr.set("")
        self.var_on.set("")
        self.var_gen.set("")



    #===search data==========
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="systerm_admin")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from adminstrator where "+str(self.var_com_search.get())+" LIKE '%" +str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)



#=============================Generate data set or Take photo Samples================
    def generate_dataset(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_on.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123", database="systerm_admin")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from adminstrator")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update adminstrator set Id=%s,Name=%s,Gen=%s,Phone=%s,Gmail=%s,Addr=%s where On_s=%s ",(  # On_s ---- _ ------ trong mysql
                                                                                                                        self.var_id.get(),
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_gen.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_gmail.get(),
                                                                                                                        self.var_addr.get(),
                                                                                                                        self.var_on.get()==id+1
                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=========================Load predifiend data on face frontals from opencv ===========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y: y+h, x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="datadmin/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)







if __name__=="__main__":
    root=Tk()
    obj=adminstator(root)
    root.mainloop()