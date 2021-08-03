from tkinter import * 
import os
from datetime import date
from time import *
from PIL import Image, ImageTk
from employee import employee_class

from product_admin import product_admin_class
from show_product import showproduct_class

class asset_management:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Asset Management Sysytem")
        self.root.config(bg='White')

        #h=str(time.strftime("%H"))
        #m=str(time.strftime("%M"))
        #s=str(time.strftime("%S"))
        

        #===title===
        self.icon_title=ImageTk.PhotoImage(Image.open(r"images/air.jpg"))

        title=Label(self.root, text="Air India", font=("algerian", 40, "bold"), image=self.icon_title, compound=LEFT, bg="red", fg="white", anchor='w', padx=30).place(x=0, y=0, relwidth=1, height=70)

        #===logout Button======
        #t = time.localtime()
        #current_time = time.strftime("%H:%M:%S", t)
        d=str(date.today())
        cur_date=d[8:10]+"-"+d[5:7]+"-"+d[0:4]
        btn_logout=Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"), bg="white", fg="red", cursor='hand2').place(x=1150, y=15, height=40, width=150)
        self.clock_label=Label(self.root, text="Welcome to the Air India\t\t  Date:"+cur_date, font=("aileron", 15), bg="red", fg="white")
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        #===Left Menu====
        self.sidevector=ImageTk.PhotoImage(Image.open(r"images/vector3.png"))

        self.menuLogo=Image.open(r"images/AirIndia_Logo.jpg")
        self.menuLogo=self.menuLogo.resize((200, 300),Image.ANTIALIAS)
        self.menuLogo=ImageTk.PhotoImage(self.menuLogo)

        LeftMenu=Frame(self.root, bd=2, width=700, height=565, bg='white')
        LeftMenu.place(x=0, y=100, width=200, height=565)

        lbl_menuLogo=Label(LeftMenu, image=self.menuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        leftM_menu=Label(LeftMenu, text="Menu", font=("algerian", 20), bg="red", fg="white").pack(side=TOP, fill=X)
        #btn_employee=Button(LeftMenu, text="Employee", font=("times new roman", 15, "bold"), command=self.employee, bg="white", image=self.sidevector, compound=LEFT, anchor='w',cursor='hand2').pack(side=TOP, fill=X)
        btn_product=Button(LeftMenu, text="Products", command=self.product, font=("times new roman", 15, "bold"), bg="white",image=self.sidevector, compound=LEFT,anchor='w',cursor='hand2').pack(side=TOP, fill=X)
        btn_show=Button(LeftMenu, text="Show\nProducts", command=self.show_product , font=("times new roman", 15, "bold"), bg="white",image=self.sidevector, compound=LEFT,anchor='w',cursor='hand2').pack(side=TOP, fill=X)
        btn_exit=Button(LeftMenu, text="Exit", command=self.exit, font=("times new roman", 15, "bold"), bg="white",image=self.sidevector, compound=LEFT, anchor='w',cursor='hand2').pack(side=TOP, fill=X)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = "Time:"+string)
            lbl.after(1000, time)
        
        # Styling the label widget so that clock
        # will look more attractive
        lbl = Label(self.root, font=("aileron", 15),background = 'red',foreground = 'white', anchor='w')
        
        # Placing clock at the centre
        # of the tkinter window
        lbl.place(x=1000, y=70, width=300, height=30)
        time()

        #=====content======

        #self.lbl_employee_centre=Label(self.root, text='Employee\t [0]',  font=('Calibri', 20, 'bold', 'italic'), bd=5, relief=RIDGE, bg='red', fg='White')
        #self.lbl_employee_centre.place(x=300, y=120, height=150, width=300)
        #self.lbl_products_centre=Label(self.root, text='Products\t [0]', font=('Calibri', 20, 'bold', 'italic'), bd=5, relief=RIDGE, bg='red', fg='White')
        #self.lbl_products_centre.place(x=605, y=120, height=150, width=300)
        #self.lbl_category_centre=Label(self.root, text='category\t [0]', font=('Calibri', 20, 'bold', 'italic'), bd=5, relief=RIDGE, bg='red', fg='White')
        #self.lbl_category_centre.place(x=910, y=120, height=150, width=300)
        #self.lbl_add_centre=Label(self.root, text='add\t [0]', font=('Calibri', 20, 'bold', 'italic'), bd=5, relief=RIDGE, bg='Black', fg='White')
        #self.lbl_add_centre.place(x=300, y=300, height=150, width=300)
    
        #self.lbl_hr=Label(self.root, text='Employee\t [0]',  font=('Calibri', 20, 'bold', 'italic'), bd=5, relief=RIDGE, bg='red', fg='White')
        
        #self.lbl_hr.place(x=300, y=120, height=150, width=300)
        #self.lbl_min=Label(self.root, text='Products\t [0]', font=('Calibri', 20, 'bold', 'italic'), bd=5, relief=RIDGE, bg='red', fg='White')
        #self.lbl_min.place(x=605, y=120, height=150, width=300)
        #self.lbl_sec=Label(self.root, text='category\t [0]', font=('Calibri', 20, 'bold', 'italic'), bd=5, relief=RIDGE, bg='red', fg='White')
        #self.lbl_sec.place(x=910, y=120, height=150, width=300)
        #lbl_add_centre=Label(self.root, text='add\t [0]', font=('Calibri', 20, 'bold', 'italic'), bd=5, relief=RIDGE, bg='Black', fg='White')
        #lbl_add_centre.place(x=300, y=300, height=150, width=300)
        
        
        
        
        
        #====footer====

        Footer=Label(self.root, text="Nikhil", font=("times new roman", 15), bg="red", fg="white").pack(side=BOTTOM, fill=X)

        

    

    
    
    
        
    
   
    def exit(self):
        self.root.destroy()
        exit()
    
        


    def logout(self):
        self.root.destroy()
        os.system("login_operation.exe")

    
    #def employee(self):

     #   self.new_win=Toplevel(self.root)
     #   self.new_obj=employee_class(self.new_win)
    
    def product(self):

        #self.new_win=Toplevel(self.root)
        #self.new_obj=product_admin_class(self.new_win)
        os.system("product.exe")
    def show_product(self):
        #self.new_win=Toplevel(self.root)
        #self.new_obj=showproduct_class(self.new_win)
        os.system("show_product.exe")
    





if __name__=="__main__":
    root=Tk()
    object=asset_management(root)

    root.mainloop()
