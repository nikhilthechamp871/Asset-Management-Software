import sqlite3
from tkinter import *

from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from tkcalendar import *
from datetime import date

import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *  # Additional Import



class employee_class:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+210+140")
        self.root.title("Employee Class")
        self.root.config(bg='White')

        #===========================
        #All Variables============

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_empID=StringVar()
        self.var_Contact=StringVar()
        self.var_Gender=StringVar()
        self.var_Name=StringVar()
        #self.var_DOB=StringVar()
        self.var_DOJ=StringVar()
        self.var_Email=StringVar()
        self.var_Password=StringVar()
        self.var_USERtype=StringVar()

        


        #=====search Frame=======

        SearchFrame=LabelFrame(self.root, text='Search Employee', font=('goudy old style', 15, 'bold'), bg='White', bd=3, relief=RIDGE)
        SearchFrame.place(x=250, y=20, height=70, width=600)

        #===options=====

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=('select', 'Name', 'EmpID', 'Contact'), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt, font=('goudy old style', 12), bg='lightyellow').place(x=240, y=10)
        btn_search=Button(SearchFrame, text='Search' ,command=self.search ,font=('goudy old style', 12), bg='lightgreen', bd=3, relief=RIDGE, cursor='hand2').place(x=410, y=6, width=150, height=30)

        #=====title=====

        title=Label(self.root, text='Employee Details', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white').place(x=50, y=100, width=1000)

        #========content========

        lbl_empid=Label(self.root, text='Emp ID', font=('goudy old style', 15), bg='white').place(x=50, y=150)
        lbl_Gender=Label(self.root, text='Gender', font=('goudy old style', 15), bg='white').place(x=350, y=150)
        lbl_Contact=Label(self.root, text='Contact', font=('goudy old style', 15), bg='white').place(x=750, y=150)

        txt_empid=Entry(self.root, textvariable=self.var_empID, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=150, width=180)
        #txt_Gender=Entry(self.root, textvariable=self.var_Gender, font=('goudy old style', 15), bg='white').place(x=500, y=150, width=180)
        cmb_Gender=ttk.Combobox(self.root,textvariable=self.var_Gender, values=('select', 'Male', 'Female', 'Other'), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_Gender.place(x=500, y=150, width=180)
        cmb_Gender.current(0)
        txt_Contact=Entry(self.root, textvariable=self.var_Contact, font=('goudy old style', 15), bg='lightyellow').place(x=850, y=150, width=180)

        lbl_Name=Label(self.root, text='Name', font=('goudy old style', 15), bg='white').place(x=50, y=200)
        #lbl_DOB=Label(self.root, text='D.O.B', font=('goudy old style', 15), bg='white').place(x=350, y=200)
        lbl_DOJ=Label(self.root, text='D.O.J', font=('goudy old style', 15), bg='white').place(x=350, y=200)

        txt_Name=Entry(self.root, textvariable=self.var_Name, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=200, width=180)
        #txt_DOB=DateEntry(self.root, textvariable=self.var_DOB, font=('goudy old style', 15), bg='lightyellow').place(x=500, y=200, width=180)

        txt_DOJ=DateEntry(self.root, textvariable=self.var_DOJ, font=('goudy old style', 15), bg='lightyellow').place(x=500, y=200, width=180)


        lbl_Email=Label(self.root, text='Email', font=('goudy old style', 15), bg='white').place(x=50, y=250)
        lbl_Password=Label(self.root, text='Password', font=('goudy old style', 15), bg='white').place(x=350, y=250)
        lbl_USERtype=Label(self.root, text='User Type', font=('goudy old style', 15), bg='white').place(x=750, y=250)

        txt_Email=Entry(self.root, textvariable=self.var_Email, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=250, width=180)
        #txt_Gender=Entry(self.root, textvariable=self.var_Gender, font=('goudy old style', 15), bg='white').place(x=500, y=150, width=180)
        cmb_USERtype=ttk.Combobox(self.root,textvariable=self.var_USERtype, values=('select', 'ADMIN', 'Employee'), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_USERtype.place(x=850, y=250, width=180)
        cmb_USERtype.current(0)
        txt_Password=Entry(self.root, textvariable=self.var_Password, font=('goudy old style', 15), bg='lightyellow').place(x=500, y=250, width=180)

        #=======================Address and Salary feature disabled as Comments========================================    
        #lbl_Address=Label(self.root, text='Address', font=('goudy old style', 15), bg='white').place(x=50, y=300)
        #lbl_Salary=Label(self.root, text='Salary', font=('goudy old style', 15), bg='white').place(x=350, y=300)

        #=====To save Address we will use text feature not entry feature because entry feature does not allow us to write in a paragraph it only allow us to wirte in horizontal diraction.

        #self.text_Address=Text(self.root, font=('goudy old style' ,15), bg='lightyellow')
        #self.text_Address.place(x=150, y=300, width=300, height=60)
        #if you want to take input Salary then simply use entry feature as used for previous variables
        #===================================================================================================================

        btn_save=Button(self.root, text='Save',command=self.add, font=('goudy old style', 12), bg='lightGreen', cursor='hand2').place(x=500, y=305, width=110, height=28)
        btn_update=Button(self.root, text='Update',command=self.update,font=('goudy old style', 12), bg='lightBlue', cursor='hand2').place(x=620, y=305, width=110, height=28)
        btn_delete=Button(self.root, text='Delete',command=self.delete, font=('goudy old style', 12), bg='Red', cursor='hand2').place(x=740, y=305, width=110, height=28)
        btn_clear=Button(self.root, text='Clear',command=self.clear, font=('goudy old style', 12), bg='yellow', cursor='hand2').place(x=860, y=305, width=110, height=28)
        
        #===========Employee Details==================
        #in this we will be using a Treeview which is efficient we can also use a list listview but treeview is more efficient==============

        emp_frame=Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.employeetable=ttk.Treeview(emp_frame, columns=("EmpID", "Name", "Email", "Gender","Contact", "DOB", "DOJ","USERtype"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.employeetable.xview)
        scrolly.config(command=self.employeetable.yview)
        #EmpID INTEGER PRIMARY KEY AUTOINCREMENT,  Name text,  Email text ,  Gender text, Contact text,  DOB text,  DOJ text, Password text,  USERtype text,  Address text,  Salary text
        self.employeetable.heading("EmpID", text='EMP ID')
        self.employeetable.heading("Name", text='Name')
        self.employeetable.heading("Email", text='Email ID')
        self.employeetable.heading("Gender", text='Gender')
        self.employeetable.heading("Contact", text='Contact')
        self.employeetable.heading("DOB", text='DOB')
        self.employeetable.heading("DOJ", text='DOJ')
        #self.employeetable.heading("Password", text='Password')
        self.employeetable.heading("USERtype", text='User Type')
        #self.employeetable.heading("Address", text='Address')
        #self.employeetable.heading("Salary", text='Salary')
        self.employeetable["show"]="headings"
        self.employeetable.pack(fill=BOTH, expand=1)

        self.employeetable.column("EmpID", width=90)
        self.employeetable.column("Name", width=100)
        self.employeetable.column("Email", width=100)
        self.employeetable.column("Gender", width=100)
        self.employeetable.column("Contact", width=100)
        self.employeetable.column("DOB", width=100)
        self.employeetable.column("DOJ", width=100)
        #self.employeetable.column("Password", width=100)
        self.employeetable.column("USERtype", width=100)
        #self.employeetable.column("Address", width=100)
        #self.employeetable.column("Salary", width=100)

        self.employeetable.pack(fill=BOTH, expand=1)
        self.employeetable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
    

    def add(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            d=str(date.today())
            
            if ((self.var_empID.get()=="") or (self.var_Email.get()=="") or (self.var_Password.get()=="") or (self.var_Contact.get()=="") or (self.var_Gender.get()=="Select") or (self.var_USERtype.get()=="Select")):
                messagebox.showerror("Error", "Mandatory fields must be filled", parent=self.root)
            try:
                int(self.var_Contact.get())

            except ValueError:
                messagebox.showerror("Error", "Only Numbers are allowed in Contact Field", parent=self.root)
            
            if (len(self.var_Contact.get())<10):
                messagebox.showerror("Error", "Contact number is incorrect", parent=self.root)
                return
            
            if (len(self.var_Password.get())<8 or len(self.var_Password.get())>16):
                messagebox.showerror("Error", "Password should have minimum of 8 characters and maximum of 16 characters", parent=self.root)
                return

            if ("@gmail.com" not in self.var_Email.get()) and ("@airindia.in" not in self.var_Email.get()) and ("@yahoo.com" not in self.var_Email.get()) and ("@outlook.com" not in self.var_Email.get()) and ("@icloud.com" not in self.var_Email.get()) and ("@gmail.co.in" not in self.var_Email.get()) and ("@yahoo.co.in" not in self.var_Email.get()) and (("@outlook.co.in" not in self.var_Email.get())):
                messagebox.showerror("Error", "Email id is INVALID. \n Enter a Valid Email id", parent=self.root)
            
                return
            

            
            
            else:
                cur.execute("Select * from employee where EmpID=?", (self.var_empID.get(),))
                row=cur.fetchone()

                if (row!=None):
                    messagebox.showerror("Error", "This employee is already exists please provide another employee id", parent=self.root)
                
                else:
                    cur.execute("Insert into employee (EmpID, Name, Email, Gender,Contact, DOJ,Password, USERtype)  values(?,?,?,?,?,?,?,?)", (
                            self.var_empID.get(),
                            self.var_Name.get(),
                            self.var_Email.get(),
                            self.var_Gender.get(),
                            self.var_Contact.get(),
                            self.var_DOJ.get(),
                            self.var_Password.get(),
                            self.var_USERtype.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Employee added sucessfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    
    def show(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.employeetable.delete(*self.employeetable.get_children())
            for row in rows:
                self.employeetable.insert('', END, values=row)

        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    
    def get_data(self, ev):

        f=self.employeetable.focus()
        content=(self.employeetable.item(f))
        row=content['values']
        self.var_empID.set(row[0])
        self.var_Name.set(row[1])
        self.var_Email.set(row[2])
        self.var_Gender.set(row[3])
        self.var_Contact.set(row[4])
        self.var_DOB.set(row[5])
        self.var_DOJ.set(row[6])
        self.var_Password.set(row[8])
        self.var_USERtype.set(row[7])
    
    def update(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if ((self.var_empID.get()=="") or (self.var_Email.get()=="") or (self.var_Password.get()=="") or (self.var_Contact.get()=="") or (self.var_Gender.get()=="Select") or (self.var_USERtype.get()=="Select")):
                messagebox.showerror("Error", "Mandatory fields must be filled", parent=self.root)
            try:
                int(self.var_Contact.get())

            except ValueError:
                messagebox.showerror("Error", "Only Numbers are allowed in Contact Field", parent=self.root)
            
            if (len(self.var_Contact.get())<10):
                messagebox.showerror("Error", "Contact number is incorrect", parent=self.root)
                return
            
            if (len(self.var_Password.get())<8 or len(self.var_Password.get())>16):
                messagebox.showerror("Error", "Password should have minimum of 8 characters and maximum of 16 characters", parent=self.root)
                return

            if ("@gmail.com" not in self.var_Email.get()) and ("@airindia.in" not in self.var_Email.get()) and ("@yahoo.com" not in self.var_Email.get()) and ("@outlook.com" not in self.var_Email.get()) and ("@icloud.com" not in self.var_Email.get()) and ("@gmail.co.in" not in self.var_Email.get()) and ("@yahoo.co.in" not in self.var_Email.get()) and (("@outlook.co.in" not in self.var_Email.get())):
                messagebox.showerror("Error", "Email id is INVALID. \nEnter a Valid Email id", parent=self.root)
            
                return
            
            
            else:
                cur.execute("Select * from employee where EmpID=?", (self.var_empID.get(),))
                row=cur.fetchone()

                if (row==None):
                    messagebox.showerror("Error", "Invalid employee id", parent=self.root)
                
                else:
                    cur.execute("Update employee set Name=?, Email=?, Gender=?,Contact=?,DOJ=?,Password=?, USERtype=? where EmpID=?", (
                            self.var_Name.get(),
                            self.var_Email.get(),
                            self.var_Gender.get(),
                            self.var_Contact.get(),
                            self.var_DOJ.get(),
                            self.var_Password.get(),
                            self.var_USERtype.get(),
                            self.var_empID.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Employee updated sucessfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if ((self.var_empID.get()=="")):
                messagebox.showerror("Error", "mandatory fields must be filled", parent=self.root)
            
            if (self.var_empID.get()=="81014023"):
                messagebox.showerror("Error", "You cannot Delete this Admin", parent=self.root)
                self.root.destroy()
                return
            
            else:
                cur.execute("Select * from employee where EmpID=?", (self.var_empID.get(),))
                row=cur.fetchone()

                if (row==None):
                    messagebox.showerror("Error", "Invalid employee id", parent=self.root)
                
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if (op==True):
                        cur.execute("Delete from employee where EmpID=?", (self.var_empID.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Details deleted sucessfully", parent=self.root)
                        self.clear()
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    
    def clear(self):
        self.var_empID.set("")
        self.var_Name.set("")
        self.var_Email.set("")
        self.var_Gender.set("Select")
        self.var_Contact.set("")
        self.var_DOJ.set("")
        self.var_Password.set("")
        self.var_USERtype.set("ADMIN")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
    

    def search(self):
        
        
        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:

            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select the search category", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search text should not be empty", parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if (len(rows)!=0):
                    self.employeetable.delete(*self.employeetable.get_children())
                    for row in rows:
                        self.employeetable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record Found", parent=self.root)

        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)















if __name__=="__main__":
    root=Tk()
    object=employee_class(root)
    root.mainloop()