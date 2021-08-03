import sqlite3

def create_database():
    con=sqlite3.connect(r'store.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(EmpID INTEGER PRIMARY KEY AUTOINCREMENT,  Name text,  Email text ,  Gender text, Contact text,DOJ text, USERtype text, Password text,   Address text,  Salary text)" )
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(sno INTEGER PRIMARY KEY AUTOINCREMENT,  Name text,  DeviceSno text UNIQUE , owner text,  Location text, SUB_Location text, Devicedetails text,  ordernum text, orderdate text,  Totalordervalue text,  DeviceValue text,  Receivedate text, Dtype text)" )
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS LOC(sno INTEGER PRIMARY KEY AUTOINCREMENT, LOCATE text)" )
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS SUBLOC(sno INTEGER PRIMARY KEY AUTOINCREMENT, SubLocation text)" )
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS ALLDEVICES(sno INTEGER PRIMARY KEY AUTOINCREMENT, DEV text)" )
    con.commit()


create_database()