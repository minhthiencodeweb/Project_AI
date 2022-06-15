from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from email.message import EmailMessage
from tkinter import messagebox
import smtplib

#https://www.google.com/settings/security/lesssecureapps
attachments = []
class Attach:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x670+0+0")
        self.root.title("face Attach")

        #Storage
        self.temp_username = StringVar()
        self.temp_password = StringVar()
        self.temp_receiver = StringVar()
        self.temp_subject = StringVar()
        self.temp_body = StringVar()


        #top image
        img=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\gmail11.png")
        img=img.resize((800,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=130)


        #bg-image
        img3=Image.open(r"C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\college_images\background-main.jpg")
        img3=img3.resize((800,670), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130, width=800, height=670)

        title_lbl=Label(bg_img,text="Send to Gmail",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=800, height=45)

        main_frame=Frame(bg_img, bd=2, bg="white")              #khung trắng
        main_frame.place(x=20, y=50, width=755, height=460)

        Content_info=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,text="Information gmail", font=("times new roman",12,"bold"))
        Content_info.place(x=25, y=10, width=700, height= 420)



        #email
        email_label=Label(Content_info,text="Email:", font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        email_entry=ttk.Entry(Content_info,textvariable=self.temp_username,width=63,font=("times new roman",13,"bold"))
        email_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #password
        pass_label=Label(Content_info,text="Password:", font=("times new roman",13,"bold"),bg="white")
        pass_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        pass_entry=ttk.Entry(Content_info,textvariable=self.temp_password,width=63,show='*',font=("times new roman",13,"bold"))
        pass_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #to
        to_label=Label(Content_info,text="To:", font=("times new roman",13,"bold"),bg="white")
        to_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        to_entry=ttk.Entry(Content_info,textvariable=self.temp_receiver,width=63,font=("times new roman",13,"bold"))
        to_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Subject
        subject_label=Label(Content_info,text="Subject:", font=("times new roman",13,"bold"),bg="white")
        subject_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        subject_entry=ttk.Entry(Content_info,textvariable=self.temp_subject,width=63,font=("times new roman",13,"bold"))
        subject_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #body
        body_label=Label(Content_info,text="Body:", font=("times new roman",13,"bold"),bg="white")
        body_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        body_entry=ttk.Entry(Content_info,textvariable=self.temp_body,width=63,font=("times new roman",13,"bold"))
        body_entry.place(x=113, y=150, width=575, height=190)
        # body_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #button
        btn_frame=Frame(Content_info, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=11, y=350, width=670, height=35)

        send_btn = Button(btn_frame, text="Send",command=self.send, width=22, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        send_btn.grid(row=0, column=0)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset, width=22, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=1)

        attach_btn = Button(btn_frame, text="Attachment",command=self.attachFile, width=22, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        attach_btn.grid(row=0, column=2)


#funtion
    def send(self):
        try:
            msg = EmailMessage()
            username = self.temp_username.get()
            password = self.temp_password.get()
            to = self.temp_receiver.get()
            subject = self.temp_subject.get()
            body = self.temp_body.get()
            msg['subject'] = subject
            msg['from'] = username
            msg['to'] = to
            msg.set_content(body)

            filename = attachments[0]

            filesend = messagebox.askyesno("Send", "Do you want to send this gmail?", parent=self.root)
            if filesend >0:
                with open(filename, 'rb') as f:
                    file_data = f.read()
                msg.add_attachment(file_data, maintype='Application',subtype='octet-stream', filename=f.name)
            else:
                return

            if username=="" or password=="" or to=="" or subject =="" or body=="":
                messagebox.showinfo("Please", "Please fill in all required information", parent=self.root)
                return
            else:
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(username,password)
                server.send_message(msg)
                messagebox.showinfo("Success", "Email has been sent successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def reset(self):
        self.temp_username.set("")
        self.temp_password.set("")
        self.temp_receiver.set("")
        self.temp_subject.set("")
        self.temp_body.set("")


    def attachFile(self):
        filename = filedialog.askopenfilename(initialdir='C:/Users/PC_MINH THIEN/PycharmProjects/PythonProjectAI2',title='Select a file')
        attachments.append(filename)


if __name__=="__main__":
    root=Tk()
    obj=Attach(root)
    root.mainloop()







