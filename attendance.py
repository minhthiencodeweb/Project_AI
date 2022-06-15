from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import shutil
from tkinter import filedialog
import os ,string ,time
from send_gmail import Attach

mydata=[]


def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference

# def send_gmail():
#     win=Tk()
#     app=Attendance(win)
#     win.mainloop()

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #=================variables=========================
        self.var_atten_id=StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


        #first image
        img=Image.open(r"college_images\logocaothang.png")
        img=img.resize((800,200), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        #second image
        img1=Image.open(r"college_images\class.jpg")
        img1=img1.resize((800,200), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        #bg-image
        img3=Image.open(r"college_images\background-main.jpg")
        img3=img3.resize((1530,710), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)


        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530, height=45)


        main_frame=Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Student Attendance Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=730, height= 580)

        img_left=Image.open(r"college_images\attentdance-stt.png")
        img_left=img_left.resize((720,130), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame=Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        #Labeland entry
        #attendance id
        attendance_label=Label(left_inside_frame,text="AttendanceId", font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white", font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)


        #Name
        nameLabel=Label(left_inside_frame,text="Name:",bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)


        #Department
        depLabel=Label(left_inside_frame,text="Department:",bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)

        #Time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        #Date
        dateLabel=Label(left_inside_frame,text="Date:",bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)


        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)


        #buttons frame
        btn_frame=Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=295, width=715, height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv, width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white" )
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete csv",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        #button frame1
        btn_frame1=Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=330, width=715, height=35)

        take_photo_btn = Button(btn_frame1,command=self.usb_data, text="Send to USB ", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1,command=self.send_gmail, text="Send to Gmail ", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)



        # Right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Attendance Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=750, y=10, width=720, height= 580)


        table_frame=Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        #============scroll bar table==================
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame, columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendane")
        self.AttendanceReportTable.heading("roll", text="StudentID")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=150)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)


        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #=====================fetch data===================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln, mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    #===Delete====
    def delete_data(self):
        try:
            delete_file = messagebox.askyesno("Delete", "Do you want to delete this student details", parent=self.root)
            filepath = (r'C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\attend.csv')
            if ((os.path.exists(filepath) == True) and (delete_file>0)):
                os.remove('attend.csv')
                global mydata
                mydata.clear()
                self.fetchData(mydata)
                self.var_atten_id.set("")
                self.var_atten_roll.set("")
                self.var_atten_name.set("")
                self.var_atten_dep.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_attendance.set("")
                messagebox.showinfo("Success","Student details successfully delete completed",parent=self.root)
                open(r'C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\attend.csv', 'w')
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


    #===reset====
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


    #===send to usb====
    def usb_data(self):
        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        print(drives)
        while True:
            uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            x = diff(uncheckeddrives, drives)
            if x:
                x = "+".join(x)
                filepath = (str(x) + "/Attend.csv")
                print(filepath)  # E:/Attend.csv
                print(os.path.exists(filepath))  # True or False
                try:
                    usb_file = messagebox.askyesno("Connect", "Connect USB successful", parent=self.root)
                    if not (os.path.exists(filepath)):
                        if (usb_file>0):
                            open(filepath, 'w')
                    shutil.copy(src=r'C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\attend.csv', dst=filepath)
                    messagebox.showinfo("Success", "Exported to USB successfully", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
                break

    def send_gmail(self):
        self.new_window=Toplevel(self.root)
        self.app=Attach(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()