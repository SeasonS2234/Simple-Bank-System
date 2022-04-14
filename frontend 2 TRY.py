from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="12345678",database="BankSystem")

def OpenAccount():
    win1 = Tk()
    win1.title("NEW ACCOUNT")
    win1.geometry("500x600")
    cid = Label(win1 , text = "Enter your preferred Customer ID : ")
    name = Label(win1 , text = "Enter you name : ")
    phone_no = Label(win1 , text = "Enter your phone number : ")
    address = Label(win1 , text = "Enter your address : ")
    acc_no= Label(win1 , text = "Enter your preferred account number : ")
    acc_type = Label(win1 , text = "Enter your Account type : ")
    bal = Label(win1 , text = "Enter your opening balance : ")
    branch_id = Label(win1 , text = "Enter branch ID : ")
    insert_button = Button(win1 , text="CREATE A NEW ACCOUNT",command=insert)
    insert_button.place(x = 180, y = 400)
    cid.place(x = 50, y =120)
    name.place(x = 50 , y = 150)
    phone_no.place(x = 50 , y = 180)
    address.place(x = 50 , y = 210)
    acc_no.place(x = 50 , y = 240)
    acc_type.place(x = 50 , y = 270)
    bal.place(x = 50 , y = 300)
    branch_id.place(x = 50 , y = 330)
    e_cid = Entry(win1)
    e_cid.place(x = 300 , y = 120)
    e_name = Entry(win1)
    e_name.place(x = 300 , y = 150)
    e_phoneno = Entry(win1)
    e_phoneno.place(x = 300 , y = 180)
    e_address = Entry(win1)
    e_address.place(x = 300 , y = 210)
    e_accno = Entry(win1)
    e_accno.place(x = 300 , y = 240)
    e_acctype = Entry(win1)
    e_acctype.place(x = 300 , y = 270)
    e_bal = Entry(win1)
    e_bal.place(x = 300 , y = 300)
    e_branchid = Entry(win1)
    e_branchid.place(x = 300 , y = 330)

def insert():
    
    Customer_Id = int(e_cid.get())
    Customer_name = e_name.get();
    Phone_no = int(e_phoneno.get());
    Address = e_address.get();
    Account_no = int(e_accno.get());
    Account_type = e_Acctype.get();
    Balance = int(e_bal.get());
    Branch_Id = e_branchid.get();
    if(cid=="" or name=="" or phone_no=="" or address=="" or acc_no=="" or acc_type=="" or bal=="" or branch_id==""):
        MessageBox.shhowinfo("Insert Status" , "All Fields are required")    
    else:
        c = con.cursor()
        data1 = (Customer_Id , Customer_name , Phone_no , Address)
        data2 = (Account_no , Account_type , Balance , Customer_Id , Branch_Id)
        sql1 = "insert into Customer values(%s,%s,%s,%s)"
        sql2 = "insert into Accounts values(%s,%s,%s,%s)"
        try:
            c.execute(sql1,data1)
            c.commit()
        except:
            c.rollback()
        try:
            c.execute(sql2,data2)
            c.commit()
        except:
            c.rollback()
        MessageBox.showinfo("Insert Status" , "New Account has been created!")
        con.close();
            
window = Tk()
window.title("Bank Management System")
window.geometry("500x700")
button1 = Button(window , text = "Open A New Account",font=("bold",12),command=OpenAccount)
button2 = Button(window , text = "Display Customer Details",font=("bold",12))
button3 = Button(window , text = "Withdraw Amount",font=("bold",12))
button4 = Button(window , text = "Deposit Amount",font=("bold",12))
button5 = Button(window , text = "Close An Account",font=("bold",12))
button6 = Button(window , text = "Exit",font=("bold",10))
button1.place(x = 100 , y = 180)
button2.place(x = 100 , y = 360)
button3.place(x = 100 , y = 540)
button4.place(x = 300 , y = 180)
button5.place(x = 300 , y = 360)
button6.place(x = 300 , y = 540)
window.mainloop()
    


        
        
