import os
import sqlite3
from sys import meta_path
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
from os import *


class login_operation:

    def __init__(self, root):
        self.back=Image.open(r"images/bg1login.jpg")
        self.back=self.back.resize((1000, 500),Image.ANTIALIAS)
        self.back=ImageTk.PhotoImage(self.back)
        self.back2=Image.open(r"images/bg2login.jpg")
        self.back2=self.back2.resize((800, 500),Image.ANTIALIAS)
        self.back2=ImageTk.PhotoImage(self.back2)
        self.back3=Image.open(r"images/bg4login.jpg")
        self.back3=self.back3.resize((800, 500),Image.ANTIALIAS)
        self.back3=ImageTk.PhotoImage(self.back3)
        self.back3=Image.open(r"images/bg4login.jpg")
        self.back3=self.back3.resize((800, 500),Image.ANTIALIAS)
        self.back3=ImageTk.PhotoImage(self.back3)
        self.back4=Image.open(r"images/bg5login.jpg")
        self.back4=self.back4.resize((800, 500),Image.ANTIALIAS)
        self.back4=ImageTk.PhotoImage(self.back4)
        self.back5=Image.open(r"images/bg7login.jpg")
        self.back5=self.back5.resize((800, 500),Image.ANTIALIAS)
        self.back5=ImageTk.PhotoImage(self.back5)
        self.label1 = Label( root, bg="white")
        self.label1.place(x = 0,y = 0)

        self.animate()
        self.root=root
        self.root.title("Login for Air India Software")
        self.root.geometry("1100x500+210+140")
        #self.root.config(bg=r"images/bg1login.jpg")
        self.login_frame_image=Image.open(r"images/logo11.png")
        self.login_frame_image=self.login_frame_image.resize((250, 150),Image.ANTIALIAS)
        self.login_frame_image=ImageTk.PhotoImage(self.login_frame_image)

        login_frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        login_frame.place(x=800, y=0, width=350, height=600)
        label_loginframe=Label(login_frame, bg="white")
        label_loginframe.place(x=10, y=0)
        label_loginframe.config(image=self.login_frame_image)

        title=Label(login_frame, text="LOGIN", font=("Elephant", 20, "bold"), fg="red" ,bg="white").place(x=0, y=150)
        lbl_user=Label(login_frame, text="Username", font=("times new roman", 15),fg="red" , bg="white").place(x=0, y=200)
        self.var_employeeid=StringVar()
        self.var_password=StringVar()

        lbl_pass=Label(login_frame, text="Password",font=("times new roman", 15),fg="red" , bg="white").place(x=0, y=300)

        txt_username=Entry(login_frame, textvariable=self.var_employeeid, font=('goudy old style', 15), bg='lightgray').place(x=0, y=250, width=180)
        txt_password=Entry(login_frame, textvariable=self.var_password, font=('goudy old style', 15), show="*", bg='lightgray').place(x=0, y=350, width=180)

        btn_login=Button(login_frame, text='Login', command=self.login, font=('goudy old style', 12), bg='red', fg="white",cursor='hand2').place(x=100, y=450, width=110, height=40)
        #btn_forget=Button(login_frame, text='Forgot Password', command=self.forget, font=('goudy old style', 12), bg='lightgray', cursor='hand2').place(x=160, y=400, width=110, height=40)



        #register_frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        #register_frame.place(x=200, y=0, height=100, width=300)

        #lbl_register=Label(register_frame, text="Don't Have an account??", font=("times new roman", 15), bg="white").place(x=0, y=0)
        #btn_login=Button(register_frame, text='Signup', font=('goudy old style', 12), bg='lightGreen', cursor='hand2').place(x=0, y=50)


    def animate(self):

        self.bg=self.back
        self.back=self.back2
        self.back2=self.back3
        self.back3=self.back4
        self.back4=self.back5
        self.back5=self.bg
        self.label1.config(image=self.bg)
        self.label1.after(2000, self.animate)




    def login(self):
        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()


        try:
            

            if self.var_employeeid.get()=="" or self.var_password.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select USERtype from employee where EmpID=? AND Password=?", (self.var_employeeid.get(), self.var_password.get()))
                user=cur.fetchone()

                if user is NONE:
                    print (user)
                    messagebox.showerror("Error", "INCORRECT USERNAME/PASSWORD", parent=self.root)
                elif user[0]=="ADMIN":
                    self.root.destroy()
                    os.system("main_template.exe")
                elif user[0]=="Employee":
                    self.root.destroy()
                    os.system("main_template_employee.exe")

            
        except Exception as ex:
            messagebox.showerror("Error", f"Invalid USERNAME/PASSWORD", parent=self.root)
            #messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def forget(self):
        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()


        try:
            

            if self.var_employeeid.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select email from employee where eid=?", (self.var_employeeid.get(),))
                email=cur.fetchone()

                if email==NONE:
                    messagebox.showerror("Error", "INCORRECT USERNAME?PASSWORD", parent=self.root)
                else:
                    #call send_email
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_confirm_pass=StringVar()

                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title("RESET PASSWORD")
                    self.forget_win.geometry("400x350+500+100")
                    self.forget_win.focus_force()

                    title=Label(self.forget_win, text='Reset PASSWORD', font=("goudy old style", 15), bg="red", fg="white").pack(side=TOP, fill=X)

                    lbl_reset=Label(self.forget_win, text="Enter OTP sent on your registered email", font=("times new roman", 15)).place(x=20, y=60)
                    text_reset=Entry(self.forget_win, textvariable=self.var_otp,font=("times new roman", 15)).place(x=20, y=100, width=250, height=30)


                    self.btn_reset=Button(self.forget_win, text="SUBMIT", font=("times new roman", 15), bg="lightblue" )
                    self.btn_reset.place(x=280, y=100, width=100, height=30)

                    lbl_new_pass=Label(self.forget_win, text="New Password", font=("times new roman", 15)).place(x=20, y=160)
                    text_new_pass=Entry(self.forget_win, textvariable=self.var_new_pass ,font=("times new roman", 15)).place(x=20, y=190, width=250, height=30)

                    lbl_confirm_pass=Label(self.forget_win, text="Confirm Password", font=("times new roman", 15)).place(x=20, y=225)
                    text_confirm_pass=Entry(self.forget_win, textvariable=self.var_confirm_pass ,font=("times new roman", 15)).place(x=20, y=255, width=250, height=30)

                    self.btn_update=Button(self.forget_win, text="Update", font=("times new roman", 15), bg="lightblue" )
                    self.btn_update.place(x=50, y=300, width=100, height=30)



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    

if __name__=="__main__":
    root=Tk()
    object=login_operation(root)
    root.mainloop()