import sqlite3
from tkinter import *
from PIL import Image, ImageTk

from tkinter import ttk, messagebox
from tkcalendar import *
import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *  # Additional Import


class showproduct_class:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+210+140")
        self.root.title("Show Product")
        self.root.config(bg='White')

        #===========================
        #All Variables============

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        '''self.var_empID=StringVar()
        self.var_contact=StringVar()
        self.var_Gender=StringVar()
        self.var_Name=StringVar()
        self.var_DOB=StringVar()
        self.var_DOJ=StringVar()
        self.var_Email=StringVar()
        self.var_Pass=StringVar()
        self.var_utype=StringVar()'''

        


        #=====search Frame=======

        SearchFrame=LabelFrame(self.root, text='Search Product', font=('goudy old style', 15, 'bold'), bg='White', bd=3, relief=RIDGE)
        SearchFrame.place(x=100, y=20, height=70, width=900)

        #===options=====

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=('select', 'Name',  'DeviceSno' , 'owner' ,  'Location' , 'Devicedetails' ,  'ordernum' , 'orderdate' ,  'Totalordervalue' ,  'DeviceValue',  'Receivedate' , 'Dtype'), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt, font=('goudy old style', 12), bg='lightyellow').place(x=240, y=10)
        btn_search=Button(SearchFrame, text='Search' ,command=self.search ,font=('goudy old style', 12), bg='lightgreen', bd=3, relief=RIDGE, cursor='hand2').place(x=410, y=6, width=150, height=30)
        
        btn_delete=Button(SearchFrame, text='Delete' ,command=self.deletedialogbox ,font=('goudy old style', 12), bg='red', bd=3, relief=RIDGE, cursor='hand2').place(x=600, y=6, width=150, height=30)

        #=====title=====

        #title=Label(self.root, text='Employee Details', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white').place(x=50, y=100, width=1000)

        #========content========

        '''lbl_empid=Label(self.root, text='Emp ID', font=('goudy old style', 15), bg='white').place(x=50, y=150)
        lbl_gender=Label(self.root, text='Gender', font=('goudy old style', 15), bg='white').place(x=350, y=150)
        lbl_contact=Label(self.root, text='Contact', font=('goudy old style', 15), bg='white').place(x=750, y=150)

        txt_empid=Entry(self.root, textvariable=self.var_empID, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=150, width=180)
        #txt_gender=Entry(self.root, textvariable=self.var_Gender, font=('goudy old style', 15), bg='white').place(x=500, y=150, width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_Gender, values=('select', 'Male', 'Female', 'Other'), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root, textvariable=self.var_contact, font=('goudy old style', 15), bg='lightyellow').place(x=850, y=150, width=180)

        lbl_Name=Label(self.root, text='Name', font=('goudy old style', 15), bg='white').place(x=50, y=200)
        lbl_DOB=Label(self.root, text='D.O.B', font=('goudy old style', 15), bg='white').place(x=350, y=200)
        lbl_DOJ=Label(self.root, text='D.O.J', font=('goudy old style', 15), bg='white').place(x=750, y=200)

        txt_Name=Entry(self.root, textvariable=self.var_Name, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=200, width=180)
        txt_DOB=Entry(self.root, textvariable=self.var_DOB, font=('goudy old style', 15), bg='lightyellow').place(x=500, y=200, width=180)

        txt_DOJ=Entry(self.root, textvariable=self.var_DOJ, font=('goudy old style', 15), bg='lightyellow').place(x=850, y=200, width=180)


        lbl_email=Label(self.root, text='Email', font=('goudy old style', 15), bg='white').place(x=50, y=250)
        lbl_pass=Label(self.root, text='Password', font=('goudy old style', 15), bg='white').place(x=350, y=250)
        lbl_utype=Label(self.root, text='User Type', font=('goudy old style', 15), bg='white').place(x=750, y=250)

        txt_email=Entry(self.root, textvariable=self.var_Email, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=250, width=180)
        #txt_gender=Entry(self.root, textvariable=self.var_Gender, font=('goudy old style', 15), bg='white').place(x=500, y=150, width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype, values=('select', 'ADMIN', 'Employee'), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_utype.place(x=850, y=250, width=180)
        cmb_utype.current(0)
        txt_pass=Entry(self.root, textvariable=self.var_Pass, font=('goudy old style', 15), bg='lightyellow').place(x=500, y=250, width=180)

        #=======================Address and salary feature disabled as Comments========================================    
        #lbl_address=Label(self.root, text='Address', font=('goudy old style', 15), bg='white').place(x=50, y=300)
        #lbl_Salary=Label(self.root, text='Salary', font=('goudy old style', 15), bg='white').place(x=350, y=300)

        #=====To save address we will use text feature not entry feature because entry feature does not allow us to write in a paragraph it only allow us to wirte in horizontal diraction.

        #self.text_address=Text(self.root, font=('goudy old style' ,15), bg='lightyellow')
        #self.text_address.place(x=150, y=300, width=300, height=60)
        #if you want to take input salary then simply use entry feature as used for previous variables
        #===================================================================================================================

        btn_save=Button(self.root, text='Save',command=self.add, font=('goudy old style', 12), bg='lightGreen', cursor='hand2').place(x=500, y=305, width=110, height=28)
        btn_update=Button(self.root, text='Update',command=self.update,font=('goudy old style', 12), bg='lightBlue', cursor='hand2').place(x=620, y=305, width=110, height=28)
        btn_delete=Button(self.root, text='Delete',command=self.delete, font=('goudy old style', 12), bg='Red', cursor='hand2').place(x=740, y=305, width=110, height=28)
        btn_clear=Button(self.root, text='Clear',command=self.clear, font=('goudy old style', 12), bg='yellow', cursor='hand2').place(x=860, y=305, width=110, height=28)
        '''
        #===========Employee Details==================
        #in this we will be using a Treeview which is efficient we can also use a list listview but treeview is more efficient==============

        productframe=Frame(self.root, bd=3, relief=RIDGE)
        productframe.place(x=0, y=100, relwidth=1, height=400)

        scrolly=Scrollbar(productframe,orient=VERTICAL)
        scrollx=Scrollbar(productframe,orient=HORIZONTAL)

        self.producttree=ttk.Treeview(productframe, columns=('sno',  'Name',  'DeviceSno' , 'owner' ,  'Location' ,'SUB_Location', 'Devicedetails' ,  'ordernum' , 'orderdate' ,  'Totalordervalue' ,  'DeviceValue',  'Receivedate' , 'Dtype' ), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.producttree.xview)
        scrolly.config(command=self.producttree.yview)

        self.producttree.heading("sno", text='Serial No')
        self.producttree.heading("Name", text='Name')
        self.producttree.heading("DeviceSno", text='Device Serial No.')
        self.producttree.heading("owner", text='Owner')
        self.producttree.heading("Location", text='Location')
        self.producttree.heading("SUB_Location", text='SUB_Location')
        self.producttree.heading("Devicedetails", text='Device Details')
        self.producttree.heading("ordernum", text='Order Number')
        self.producttree.heading("orderdate", text='Order Date')
        self.producttree.heading("Totalordervalue", text='Total Order Value')
        self.producttree.heading("DeviceValue", text='Device Value')
        self.producttree.heading("Receivedate", text='Receive Date')
        self.producttree.heading("Dtype", text='Device Type')
        self.producttree["show"]="headings"
        self.producttree.pack(fill=BOTH, expand=1)

        self.producttree.column("sno", width=90)
        self.producttree.column("Name", width=100)
        self.producttree.column("DeviceSno", width=100)
        self.producttree.column("owner", width=100)
        self.producttree.column("Location", width=100)
        self.producttree.column("SUB_Location", width=150)
        self.producttree.column("Devicedetails", width=100)
        self.producttree.column("ordernum", width=100)
        self.producttree.column("orderdate", width=100)
        self.producttree.column("Totalordervalue", width=100)
        self.producttree.column("DeviceValue", width=100)
        self.producttree.column("Receivedate", width=100)
        self.producttree.column("Dtype", width=100)

        self.producttree.pack(fill=BOTH, expand=1)
        self.producttree.bind("<ButtonRelease-1>", self.edit_data)
        self.show()
    

    
    def show(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.producttree.delete(*self.producttree.get_children())
            for row in rows:
                self.producttree.insert('', END, values=row)

        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    

    
    


    def search(self):
        
        
        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:

            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select the search category", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search text should not be empty", parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                print (rows)
                if (len(rows)!=0):
                    self.producttree.delete(*self.producttree.get_children())
                    for row in rows:
                        self.producttree.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record Found", parent=self.root)

        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    

    def deletedialogbox(self):


        try:
            #call send_email
            self.var_targetsno=StringVar()
            #self.var_new_pass=StringVar()
            #self.var_confirm_pass=StringVar()

            self.delete_win=Toplevel(self.root)
            self.delete_win.title("DELETE FROM THE RECORDS")
            self.delete_win.geometry("400x350+500+100")
            self.delete_win.focus_force()

            title=Label(self.delete_win, text='DELETE THE RECORD', font=("goudy old style", 15), bg="darkblue", fg="white").pack(side=TOP, fill=X)

            #lbl_reset=Label(self.delete_win, text="Enter OTP sent on your registered email", font=("times new roman", 15)).place(x=20, y=60)
            #text_reset=Entry(self.delete_win, textvariable=self.var_otp,font=("times new roman", 15)).place(x=20, y=100, width=250, height=30)


            #self.btn_reset=Button(self.delete_win, text="SUBMIT", font=("times new roman", 15), bg="lightblue" )
            #self.btn_reset.place(x=280, y=100, width=100, height=30)

            lbl_new_pass=Label(self.delete_win, text="Device Unique Serial Number", font=("times new roman", 15)).place(x=80, y=50)
            text_new_pass=Entry(self.delete_win, textvariable=self.var_targetsno ,font=("times new roman", 15)).place(x=65, y=80, width=270, height=30)

            #lbl_confirm_pass=Label(self.delete_win, text="Confirm Password", font=("times new roman", 15)).place(x=20, y=225)
            #text_confirm_pass=Entry(self.delete_win, textvariable=self.var_confirm_pass ,font=("times new roman", 15)).place(x=20, y=255, width=250, height=30)
            
            self.btn_delete=Button(self.delete_win, text="Delete", command=self.delete, font=("times new roman", 15), bg="lightblue" )
            self.btn_delete.place(x=80, y=200, width=100, height=30)
            #self.btn_close=Button(self.delete_win, text="Close", command=self.exitproductadmin, font=("times new roman", 15), bg="lightblue" )
            #self.btn_close.place(x=200, y=200, width=100, height=30)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    

    def delete(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if ((self.var_targetsno.get()=="")):
                messagebox.showerror("Error", "mandatory fields must be filled", parent=self.root)
            
            else:
                cur.execute("Select * from product where DeviceSno=?", (self.var_targetsno.get(),))
                row=cur.fetchone()

                if (row==None):
                    messagebox.showerror("Error", "Invalid Device Serial Number", parent=self.root)
                
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if (op==True):
                        cur.execute("Delete from product where DeviceSno=?", (self.var_targetsno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Products Details deleted sucessfully", parent=self.root)
                        #self.clear()
                        self.show()
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    
    def edit_data(self, ev):
        try:
            #call send_email
            self.var_targetsno=StringVar()
            #self.var_new_pass=StringVar()
            #self.var_confirm_pass=StringVar()

            self.edit_win=Toplevel(self.root)
            self.edit_win.title("DELETE FROM THE RECORDS")
            self.edit_win.geometry("1100x600+100+100")
            self.edit_win.focus_force()
            self.var_Device=StringVar()
            self.var_Serialno=StringVar()
            self.var_Location=StringVar()
            self.var_sublocation=StringVar()
            self.var_Dtype=StringVar()
            self.var_DDetails=StringVar()
            self.var_MakenModel=StringVar()
            self.var_Ordernum=StringVar()
            self.var_orderdate=StringVar()
            self.var_totalordervalue=StringVar()
            self.var_DeviceValue=StringVar()
            self.var_Recdate=StringVar()
            self.var_owner=StringVar()

            title=Label(self.edit_win, text='DELETE THE RECORD', font=("goudy old style", 15), bg="darkblue", fg="white").pack(side=TOP, fill=X)

            Label_Note=Label(self.edit_win, text='(* denotes that fields are Mandatory)', font=('times new roman', 12), bg='#B6B2B1', fg="red").place(x=10, y=360)
            Label_Device=Label(self.edit_win, text='Device name*', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=20, y=60)
            Label_owner=Label(self.edit_win, text='Owner',font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=740, y=60)
            Label_Serialno=Label(self.edit_win, text='Device Serial Number*', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=350, y=60)
            Label_Location=Label(self.edit_win, text='Location*', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=20, y=130)
            Label_Dtype=Label(self.edit_win, text='Model Number*', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=350, y=300)
            Label_DDetails=Label(self.edit_win, text='Device\nDetails', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=740, y=300)
            #Label_MakenMOdel=Label(self.edit_win, text='MAKE AND MODEL', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=350, y=370)
            Label_Order_Number=Label(self.edit_win, text='Order Number*', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=20, y=210)
            Label_OrderDate=Label(self.edit_win, text='Order Date*', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=734, y=130)
            Label_TotalorderValue=Label(self.edit_win, text='Total Order Value*', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=350, y=210)
            Label_DeviceValue=Label(self.edit_win, text='Device Value', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=20, y=300)
            Label_Receivedate=Label(self.edit_win, text='Receive Date', font=('times new roman', 15, 'bold'), bg='lightgrey').place(x=350, y=130)
            Label_sublocation=Label(self.edit_win, text='Sub Location', font=('times new roman', 15, 'bold'), bg='white').place(x=740, y=210)


            self.dynamicsublocation,self.dynamicoffices_list, self.dynamicdevices_list=self.get_offices()
            #lbl_reset=Label(self.edit_win, text="Enter OTP sent on your registered email", font=("times new roman", 15)).place(x=20, y=60)
            #text_reset=Entry(self.edit_win, textvariable=self.var_otp,font=("times new roman", 15)).place(x=20, y=100, width=250, height=30)
            
            #txt_DeviceName=Entry(product_Frame, textvariable=self.var_Device, font=('goudy old style', 15), bg='lightyellow').place(x=160, y=60, width=180)
            cmb_dynamicdev=ttk.Combobox(self.edit_win,textvariable=self.var_Device, values=(["Select"]+self.dynamicdevices_list), state='readonly', justify=CENTER, font=('times new roman', 13))
            cmb_dynamicdev.place(x=160, y=60, width=180)
            cmb_dynamicdev.current(0)
            txt_serialnum=Entry(self.edit_win, textvariable=self.var_Serialno, font=('goudy old style', 15), bg='lightyellow').place(x=550, y=60, width=180)
            txt_owner=Entry(self.edit_win, textvariable=self.var_owner, font=('goudy old style', 15), bg='lightyellow').place(x=850, y=60, width=180)
            cmb_loc=ttk.Combobox(self.edit_win,textvariable=self.var_Location, values=(["Select"]+self.dynamicoffices_list), state='readonly', justify=CENTER, font=('times new roman', 13))
            cmb_loc.place(x=160, y=130, width=180)
            cmb_loc.current(0)
            
            #txt_MnM=Entry(self.edit_win, textvariable=self.var_MakenModel, font=('goudy old style', 15), bg='lightyellow').place(x=550, y=130, width=180)

            #==========second row===========

            txt_ordernum=Entry(self.edit_win, textvariable=self.var_Ordernum, font=('goudy old style', 15), bg='lightyellow').place(x=160, y=210, width=180)
            txt_orderdate=DateEntry(self.edit_win, textvariable=self.var_orderdate, font=('goudy old style', 15), bg='lightyellow').place(x=850, y=130, width=180)
            txt_recdate=DateEntry(self.edit_win, textvariable=self.var_Recdate, font=('goudy old style', 15), bg='lightyellow').place(x=550, y=130, width=180)


            #=====third row=======
            txt_devicevalue=Entry(self.edit_win, textvariable=self.var_DeviceValue, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=300, width=180)
            txt_totalordervalue=Entry(self.edit_win, textvariable=self.var_totalordervalue, font=('goudy old style', 15), bg='lightyellow').place(x=550, y=210, width=180)
            cmb_subloc=ttk.Combobox(self.edit_win,textvariable=self.var_sublocation, values=(["Select"]+self.dynamicsublocation), state='readonly', justify=CENTER, font=('times new roman', 13))
            cmb_subloc.place(x=870, y=210, width=180)
            cmb_subloc.current(0)
            #=========fourth row===========
            #cmb_dtype=ttk.Combobox(self.edit_win,textvariable=self.var_Dtype, values=('select', 'Hardware', 'Software'), state='readonly', justify=CENTER, font=('times new roman', 13))
            #cmb_dtype.place(x=550, y=300, width=150)
            #cmb_dtype.current(0)
            xt_Dtype=Entry(self.edit_win, textvariable=self.var_Dtype,  font=('goudy old style', 15), bg='lightyellow').place(x=550, y=300, width=180)

            #btn_save=Button(self.edit_win, text='Save', command=self.add, font=('goudy old style', 12), bg='lightGreen', cursor='hand2').place(x=70, y=400, width=110, height=40)
            btn_update=Button(self.edit_win, text='Update', command=self.update, font=('goudy old style', 12), bg='lightBlue', cursor='hand2').place(x=200, y=400, width=110, height=40)
            btn_delete=Button(self.edit_win, text='Delete', command=self.delete, font=('goudy old style', 12), bg='Red', cursor='hand2').place(x=330, y=400, width=110, height=40)
            btn_clear=Button(self.edit_win, text='Clear', command=self.clear, font=('goudy old style', 12), bg='yellow', cursor='hand2').place(x=460, y=400, width=110, height=40)
            #btn_addloc=Button(self.edit_win, text='ADD LOCATION', command=self.addlocadmin, font=('goudy old style', 12, 'bold'), bg='darkblue', fg="white",cursor='hand2').place(x=740, y=400, width=150, height=40)
            #btn_adddevice=Button(self.edit_win, text='ADD NEW DEVICE', command=self.adddevadmin, font=('goudy old style', 12, 'bold'), bg='darkblue', fg="white", cursor='hand2').place(x=900, y=400, width=150, height=40)
            #btn_addsubloc=Button(self.edit_win, text='ADD SUB LOCATION', command=self.sublocadmin, font=('goudy old style', 12, 'bold'), bg='darkblue', fg="white",cursor='hand2').place(x=580, y=400, width=150, height=40)

            self.text_ddetails=Entry(self.edit_win, textvariable=self.var_DDetails, font=('goudy old style', 15), bg='lightyellow')
            self.text_ddetails.place(x=850, y=310, width=180)
            f=self.producttree.focus()
            content=(self.producttree.item(f))
            row=content['values']
            print (row)
            self.var_Device.set(row[1])
            self.var_Serialno.set(row[2])
            self.var_owner.set(row[3])
            self.var_Location.set(row[4])
            self.var_sublocation.set(row[5])
            self.var_DDetails.set(row[6])
            self.var_Ordernum.set(row[7])
            self.var_orderdate.set(row[8])
            self.var_totalordervalue.set(row[9])
            self.var_DeviceValue.set(row[10])
            self.var_Recdate.set(row[11])
            self.var_Dtype.set(row[12])
            


            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    



    
    def add(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if (self.var_Serialno.get()=="" or self.var_Device.get()=="Select" or self.var_Location.get()=="Select" or self.var_orderdate.get()=="" or self.var_Ordernum.get()=="" or self.var_Dtype.get()=="" or self.var_totalordervalue.get()==""):
                messagebox.showerror("Error", "mandatory fields must be filled", parent=self.root)
            
            else:
                cur.execute("Select * from product where sno=?", (self.var_Serialno.get(),))
                row=cur.fetchone()

                if (row!=None):
                    messagebox.showerror("Error", "This device is already exists please provide another employee id", parent=self.root)
                
                else:
                    cur.execute("Insert into product (Name, DeviceSno, owner ,  Location ,SUB_Location, Devicedetails ,  ordernum , orderdate ,  Totalordervalue ,  DeviceValue,  Receivedate, Dtype)  values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                            self.var_Device.get(),
                            self.var_Serialno.get(),
                            self.var_owner.get(),
                            self.var_Location.get(),
                            self.var_sublocation.get(),
                            self.text_ddetails.get('1.0',END),
                            self.var_Ordernum.get(),
                            self.var_orderdate.get(),
                            self.var_totalordervalue.get(),
                            self.var_DeviceValue.get(),
                            self.var_Recdate.get(),
                            self.var_Dtype.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Product added sucessfully", parent=self.root)
                    #self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)




    def update(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if (self.var_Serialno.get()=="" or self.var_Device.get()=="Select" or self.var_Location.get()=="Select" or self.var_orderdate.get()=="" or self.var_Ordernum.get()=="" or self.var_Dtype.get()=="" or self.var_totalordervalue.get()==""):
                messagebox.showerror("Error", "mandatory fields must be filled", parent=self.root)
            
            else:
                cur.execute("Select * from product where DeviceSno=?", (self.var_Serialno.get(),))
                row=cur.fetchone()

                if (row==None):
                    messagebox.showerror("Error", "Invalid Serial No", parent=self.root)
                
                else:
                    cur.execute("Update product set Name=?,owner=? ,  Location=? , Devicedetails=? ,  ordernum=? , orderdate=? ,  Totalordervalue=? ,  DeviceValue=?,  Receivedate=?, Dtype=? where DeviceSno=?", (
                            self.var_Device.get(),
                            self.var_owner.get(),
                            self.var_Location.get(),
                            self.var_DDetails.get(),
                            self.var_Ordernum.get(),
                            self.var_orderdate.get(),
                            self.var_totalordervalue.get(),
                            self.var_DeviceValue.get(),
                            self.var_Recdate.get(),
                            self.var_Dtype.get(),
                            self.var_Serialno.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Product updated sucessfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if ((self.var_Serialno.get()=="")):
                messagebox.showerror("Error", "mandatory fields must be filled", parent=self.root)
            
            else:
                cur.execute("Select * from product where DeviceSno=?", (self.var_Serialno.get(),))
                row=cur.fetchone()

                if (row==None):
                    messagebox.showerror("Error", "Invalid employee id", parent=self.root)
                
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if (op==True):
                        cur.execute("Delete from product where DeviceSno=?", (self.var_Serialno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Details deleted sucessfully", parent=self.root)
                        self.clear()
                        self.show()
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_Device.set("Select")
        self.var_Serialno.set("")
        self.var_owner.set("")
        self.var_Location.set("Select")
        self.var_Ordernum.set("")
        self.var_Recdate.set("")
        self.var_DeviceValue.set("")
        self.var_orderdate.set("")
        self.var_totalordervalue.set("")
        self.var_DDetails.set("")
        self.var_Dtype.set("Select")
        #self.var_searchtxt.set("")
        #self.var_searchby.set("Select")
        #self.show()



        

    def get_offices(self):
        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()
        cur2=con.cursor()
        cur3=con.cursor()

        cur.execute("Select LOCATE from LOC")
        cur2.execute("Select DEV from ALLDEVICES")
        cur3.execute("Select SubLocation from SUBLOC")
        
        row=cur.fetchall()
        devices=cur2.fetchall()
        slocs=cur3.fetchall()

        offices=[]
        for office in row:
            offices.append(office[0])
        alldev=[]
        for d in devices:
            alldev.append(d[0])
        sl=[]
        for sloc in slocs:
            sl.append(sloc[0])
        
        

        
        #print (offices)
        #print (alldev)
        return sl,offices,alldev
    
    def show(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.producttree.delete(*self.producttree.get_children())
            for row in rows:
                self.producttree.insert('', END, values=row)

        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)









if __name__=="__main__":
    root=Tk()
    object=showproduct_class(root)
    root.mainloop()