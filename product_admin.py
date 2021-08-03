
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os
from tkcalendar import *
import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *  # Additional Import


class product_admin_class:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+210+140")
        self.root.title("product Class")
        self.root.config(bg='White')

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


        product_Frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_Frame.place(x=10, y=10, width=1080, height=480)

        #========TITLE=========
        title=Label(product_Frame, text='Product Details', font=('times new roman', 15, 'bold'), bg='darkblue', fg='white').pack(side=TOP, fill=X)


        Label_Note=Label(product_Frame, text='(* denotes that fields are Mandatory)', font=('times new roman', 12), bg='white', fg="red").place(x=10, y=360)
        Label_Device=Label(product_Frame, text='Device name*', font=('times new roman', 15, 'bold'), bg='white').place(x=20, y=60)
        Label_owner=Label(product_Frame, text='Owner',font=('times new roman', 15, 'bold'), bg='white').place(x=740, y=60)
        Label_Serialno=Label(product_Frame, text='Device Serial Number*', font=('times new roman', 15, 'bold'), bg='white').place(x=350, y=60)
        Label_Location=Label(product_Frame, text='Location*', font=('times new roman', 15, 'bold'), bg='white').place(x=20, y=130)
        Label_Dtype=Label(product_Frame, text='Model Number*', font=('times new roman', 15, 'bold'), bg='white').place(x=350, y=300)
        Label_DDetails=Label(product_Frame, text='Device\nDetails', font=('times new roman', 15, 'bold'), bg='white').place(x=740, y=300)
        #Label_MakenMOdel=Label(product_Frame, text='MAKE AND MODEL', font=('times new roman', 15, 'bold'), bg='white').place(x=350, y=370)
        Label_Order_Number=Label(product_Frame, text='Order Number*', font=('times new roman', 15, 'bold'), bg='white').place(x=20, y=210)
        Label_OrderDate=Label(product_Frame, text='Order Date*', font=('times new roman', 15, 'bold'), bg='white').place(x=734, y=130)
        Label_TotalorderValue=Label(product_Frame, text='Total Order Value*', font=('times new roman', 15, 'bold'), bg='white').place(x=350, y=210)
        Label_DeviceValue=Label(product_Frame, text='Device Value', font=('times new roman', 15, 'bold'), bg='white').place(x=20, y=300)
        Label_Receivedate=Label(product_Frame, text='Receive Date', font=('times new roman', 15, 'bold'), bg='white').place(x=350, y=130)
        Label_sublocation=Label(product_Frame, text='Sub Location', font=('times new roman', 15, 'bold'), bg='white').place(x=740, y=210)

        #combo box are for location and device type
        #rest entries will be taken by entry feature
        #=====first row=========
        self.dynamicsublocation,self.dynamicoffices_list, self.dynamicdevices_list=self.get_offices()
        #txt_DeviceName=Entry(product_Frame, textvariable=self.var_Device, font=('goudy old style', 15), bg='lightyellow').place(x=160, y=60, width=180)
        cmb_dynamicdev=ttk.Combobox(product_Frame,textvariable=self.var_Device, values=(["Select"]+self.dynamicdevices_list), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_dynamicdev.place(x=160, y=60, width=180)
        cmb_dynamicdev.current(0)
        txt_serialnum=Entry(product_Frame, textvariable=self.var_Serialno, font=('goudy old style', 15), bg='lightyellow').place(x=550, y=60, width=180)
        txt_owner=Entry(product_Frame, textvariable=self.var_owner, font=('goudy old style', 15), bg='lightyellow').place(x=850, y=60, width=180)
        cmb_loc=ttk.Combobox(product_Frame,textvariable=self.var_Location, values=(["Select"]+self.dynamicoffices_list), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_loc.place(x=160, y=130, width=180)
        cmb_loc.current(0)
        
        #txt_MnM=Entry(product_Frame, textvariable=self.var_MakenModel, font=('goudy old style', 15), bg='lightyellow').place(x=550, y=130, width=180)

        #==========second row===========

        txt_ordernum=Entry(product_Frame, textvariable=self.var_Ordernum, font=('goudy old style', 15), bg='lightyellow').place(x=160, y=210, width=180)
        txt_orderdate=DateEntry(product_Frame, textvariable=self.var_orderdate, font=('goudy old style', 15), bg='lightyellow').place(x=850, y=130, width=180)
        txt_recdate=DateEntry(product_Frame, textvariable=self.var_Recdate, font=('goudy old style', 15), bg='lightyellow').place(x=550, y=130, width=180)


        #=====third row=======
        txt_devicevalue=Entry(product_Frame, textvariable=self.var_DeviceValue, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=300, width=180)
        txt_totalordervalue=Entry(product_Frame, textvariable=self.var_totalordervalue, font=('goudy old style', 15), bg='lightyellow').place(x=550, y=210, width=180)
        cmb_subloc=ttk.Combobox(product_Frame,textvariable=self.var_sublocation, values=(["Select"]+self.dynamicsublocation), state='readonly', justify=CENTER, font=('times new roman', 13))
        cmb_subloc.place(x=870, y=210, width=180)
        cmb_subloc.current(0)

        #=========fourth row===========
        #cmb_dtype=ttk.Combobox(product_Frame,textvariable=self.var_Dtype, values=('select', 'Hardware', 'Software'), state='readonly', justify=CENTER, font=('times new roman', 13))
        #cmb_dtype.place(x=550, y=300, width=150)
        #cmb_dtype.current(0)
        txt_Dtype=Entry(product_Frame, textvariable=self.var_Dtype,  font=('goudy old style', 15), bg='lightyellow').place(x=550, y=300, width=180)
        self.text_ddetails=Text(self.root, font=('goudy old style' ,15), bg='lightyellow')
        self.text_ddetails.place(x=850, y=310, width=200, height=60)


        #=======buttons=======
        

        btn_save=Button(product_Frame, text='Save', command=self.add, font=('goudy old style', 12), bg='lightGreen', cursor='hand2').place(x=70, y=400, width=110, height=40)
        btn_update=Button(product_Frame, text='Update', command=self.update, font=('goudy old style', 12), bg='lightBlue', cursor='hand2').place(x=200, y=400, width=110, height=40)
        btn_delete=Button(product_Frame, text='Delete', command=self.delete, font=('goudy old style', 12), bg='Red', cursor='hand2').place(x=330, y=400, width=110, height=40)
        btn_clear=Button(product_Frame, text='Clear', command=self.clear, font=('goudy old style', 12), bg='yellow', cursor='hand2').place(x=460, y=400, width=110, height=40)
        btn_addloc=Button(product_Frame, text='ADD LOCATION', command=self.addlocadmin, font=('goudy old style', 12, 'bold'), bg='darkblue', fg="white",cursor='hand2').place(x=740, y=400, width=150, height=40)
        btn_adddevice=Button(product_Frame, text='ADD NEW DEVICE', command=self.adddevadmin, font=('goudy old style', 12, 'bold'), bg='darkblue', fg="white", cursor='hand2').place(x=900, y=400, width=150, height=40)
        btn_addsubloc=Button(product_Frame, text='ADD SUB LOCATION', command=self.sublocadmin, font=('goudy old style', 10, 'bold'), bg='darkblue', fg="white",cursor='hand2').place(x=580, y=400, width=150, height=40)

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
                    #self.show()
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
    

    def addlocadmin(self):


        try:
            #call send_email
            self.var_newlocation=StringVar()
            #self.var_new_pass=StringVar()
            #self.var_confirm_pass=StringVar()

            self.forget_win=Toplevel(self.root)
            self.forget_win.title("ADD LOCATION")
            self.forget_win.geometry("400x350+500+100")
            self.forget_win.focus_force()

            title=Label(self.forget_win, text='ADD LOCATION', font=("goudy old style", 15), bg="darkblue", fg="white").pack(side=TOP, fill=X)

            #lbl_reset=Label(self.forget_win, text="Enter OTP sent on your registered email", font=("times new roman", 15)).place(x=20, y=60)
            #text_reset=Entry(self.forget_win, textvariable=self.var_otp,font=("times new roman", 15)).place(x=20, y=100, width=250, height=30)


            #self.btn_reset=Button(self.forget_win, text="SUBMIT", font=("times new roman", 15), bg="lightblue" )
            #self.btn_reset.place(x=280, y=100, width=100, height=30)

            lbl_new_pass=Label(self.forget_win, text="New Location", font=("times new roman", 15)).place(x=140, y=50)
            text_new_pass=Entry(self.forget_win, textvariable=self.var_newlocation ,font=("times new roman", 15)).place(x=65, y=80, width=270, height=30)

            #lbl_confirm_pass=Label(self.forget_win, text="Confirm Password", font=("times new roman", 15)).place(x=20, y=225)
            #text_confirm_pass=Entry(self.forget_win, textvariable=self.var_confirm_pass ,font=("times new roman", 15)).place(x=20, y=255, width=250, height=30)
            
            self.btn_update=Button(self.forget_win, text="ADD", command=self.addlocation, font=("times new roman", 15), bg="lightblue" )
            self.btn_update.place(x=80, y=200, width=100, height=30)
            self.btn_close=Button(self.forget_win, text="Close", command=self.exitproductadmin, font=("times new roman", 15), bg="lightblue" )
            self.btn_close.place(x=200, y=200, width=100, height=30)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    
    def sublocadmin(self):
        try:
            #call send_email
            self.var_newsublocation=StringVar()
            #self.var_newlocation=StringVar()
            #self.var_new_pass=StringVar()
            #self.var_confirm_pass=StringVar()

            self.editsub_win=Toplevel(self.root)
            self.editsub_win.title("ADD LOCATION")
            self.editsub_win.geometry("400x350+500+100")
            self.editsub_win.focus_force()

            title=Label(self.editsub_win, text='ADD SUB LOCATION', font=("goudy old style", 15), bg="darkblue", fg="white").pack(side=TOP, fill=X)

            #lbl_reset=Label(self.editsub_win, text="Enter OTP sent on your registered email", font=("times new roman", 15)).place(x=20, y=60)
            #text_reset=Entry(self.editsub_win, textvariable=self.var_otp,font=("times new roman", 15)).place(x=20, y=100, width=250, height=30)


            #self.btn_reset=Button(self.editsub_win, text="SUBMIT", font=("times new roman", 15), bg="lightblue" )
            #self.btn_reset.place(x=280, y=100, width=100, height=30)

            lbl_new_pass=Label(self.editsub_win, text="New sub Location", font=("times new roman", 15)).place(x=140, y=50)
            text_new_pass=Entry(self.editsub_win, textvariable=self.var_newsublocation ,font=("times new roman", 15)).place(x=65, y=80, width=270, height=30)

            #lbl_confirm_pass=Label(self.editsub_win, text="Confirm Password", font=("times new roman", 15)).place(x=20, y=225)
            #text_confirm_pass=Entry(self.editsub_win, textvariable=self.var_confirm_pass ,font=("times new roman", 15)).place(x=20, y=255, width=250, height=30)
            
            self.btn_update=Button(self.editsub_win, text="ADD", command=self.addsublocation, font=("times new roman", 15), bg="lightblue" )
            self.btn_update.place(x=80, y=200, width=100, height=30)
            self.btn_close=Button(self.editsub_win, text="Close", command=self.exitproductadmin, font=("times new roman", 15), bg="lightblue" )
            self.btn_close.place(x=200, y=200, width=100, height=30)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    

    def adddevadmin(self):
        try:
            #call send_email
            self.var_newdevice=StringVar()
            #self.var_new_pass=StringVar()
            #self.var_confirm_pass=StringVar()

            self.device_win=Toplevel(self.root)
            self.device_win.title("ADD NEW DEVICE")
            self.device_win.geometry("400x350+500+100")
            self.device_win.focus_force()

            title=Label(self.device_win, text='ADD NEW DEVICE', font=("goudy old style", 15), bg="darkblue", fg="white").pack(side=TOP, fill=X)

            #lbl_reset=Label(self.device_win, text="Enter OTP sent on your registered email", font=("times new roman", 15)).place(x=20, y=60)
            #text_reset=Entry(self.device_win, textvariable=self.var_otp,font=("times new roman", 15)).place(x=20, y=100, width=250, height=30)


            #self.btn_reset=Button(self.device_win, text="SUBMIT", font=("times new roman", 15), bg="lightblue" )
            #self.btn_reset.place(x=280, y=100, width=100, height=30)

            lbl_new_pass=Label(self.device_win, text="Device Name", font=("times new roman", 15)).place(x=140, y=50)
            text_new_pass=Entry(self.device_win, textvariable=self.var_newdevice ,font=("times new roman", 15)).place(x=65, y=80, width=270, height=30)

            #lbl_confirm_pass=Label(self.device_win, text="Confirm Password", font=("times new roman", 15)).place(x=20, y=225)
            #text_confirm_pass=Entry(self.device_win, textvariable=self.var_confirm_pass ,font=("times new roman", 15)).place(x=20, y=255, width=250, height=30)
            
            self.btn_update=Button(self.device_win, text="ADD", command=self.adddevice, font=("times new roman", 15), bg="lightblue" )
            self.btn_update.place(x=80, y=200, width=100, height=30)
            self.btn_close=Button(self.device_win, text="Close", command=self.exitsublocadmin, font=("times new roman", 15), bg="lightblue" )
            self.btn_close.place(x=220, y=200, width=100, height=30)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    

    
    
    
    def exitproductadmin(self):
        self.forget_win.destroy()
    
    def exitdeviceadmin(self):
        self.device_win.destroy()
    
    def exitsublocadmin(self):
        self.editsub_win.destroy()

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


    def addlocation(self):

        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if ((self.var_newlocation.get()=="")):
                messagebox.showerror("Error", "mandatory fields must be filled", parent=self.root)
            
            else:
                cur.execute("Select * from LOC where LOCATE=?", (self.var_newlocation.get(),))
                row=cur.fetchone()

                if (row!=None):
                    messagebox.showerror("Error", "This location is already exists please provide another location", parent=self.root)
                
                else:
                    self.caplocation=self.var_newlocation.get()
                    #self.caplocation=self.caplocation.upper()
                    cur.execute("Insert into LOC(LOCATE)  values(?)", (
                            self.caplocation.upper(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Location added sucessfully", parent=self.root)
                    #self.show()
                    self.get_offices()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    
    def addsublocation(self):
        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if ((self.var_newsublocation.get()=="")):
                messagebox.showerror("Error", "mandatory fields must be filled", parent=self.root)
            
            else:
                cur.execute("Select * from SUBLOC where SubLocation=?", (self.var_newsublocation.get(),))
                row=cur.fetchone()

                if (row!=None):
                    messagebox.showerror("Error", "This location is already exists please provide another location", parent=self.root)
                
                else:
                    self.caplocation=self.var_newsublocation.get()
                    #self.caplocation=self.caplocation.upper()
                    cur.execute("Insert into SUBLOC(SubLocation)  values(?)", (
                            self.caplocation.upper(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "SUB Location added sucessfully", parent=self.root)
                    #self.show()
                    self.get_offices()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



    def adddevice(self):
        con=sqlite3.connect(database=r'store.db')
        cur=con.cursor()

        try:
            if ((self.var_newdevice.get()=="")):
                messagebox.showerror("Error", "mandatory fields must be filled", parent=self.root)
            
            else:
                cur.execute("Select * from ALLDEVICES where DEV=?", (self.var_newdevice.get(),))
                row=cur.fetchone()

                if (row!=None):
                    messagebox.showerror("Error", "This device is already exists please provide another device", parent=self.root)
                
                else:
                    self.capdevice=self.var_newdevice.get()
                    #self.caplocation=self.caplocation.upper()
                    cur.execute("Insert into ALLDEVICES(DEV)  values(?)", (
                            self.capdevice.upper(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "Device added sucessfully", parent=self.root)
                    #self.show()
                    self.get_offices()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    
        
    

    


 





        





if __name__=="__main__":
    root=Tk()
    object=product_admin_class(root)
    root.mainloop()