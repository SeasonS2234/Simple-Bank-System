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
    global e_cid
    global e_name
    global e_phoneno
    global e_address
    global e_accno
    global e_acctype
    global e_bal
    global e_branchid
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
    Customer_Id = e_cid.get()
    Customer_name = e_name.get();
    Phone_no = e_phoneno.get();
    Address = e_address.get();
    Account_no = e_accno.get();
    Account_type = e_acctype.get();
    Balance = e_bal.get();
    Branch_Id = e_branchid.get();    
    if(Customer_Id=="" or Customer_name=="" or Phone_no=="" or Address=="" or Account_no=="" or Account_type=="" or Balance=="" or Branch_Id==""):
        MessageBox.showinfo("Insert Status" , "All Fields are required")
    else:
        c = con.cursor()
        data1 = (Customer_Id , Customer_name , Phone_no , Address)
        data2 = (Account_no , Account_type , Balance , Customer_Id , Branch_Id)
        sql1 = "insert into Customer values(%s,%s,%s,%s)"
        sql2 = "insert into Accounts values(%s,%s,%s,%s,%s)"
        c.execute(sql1,data1)
        c.execute(sql2,data2)
        c.execute("commit");
        MessageBox.showinfo("Insert Status" , "New Account has been created!")
        con.close();
def DepositAmount():
    win2 = Tk()
    win2.title("Deposit Amount")
    win2.geometry("500x600")
    ano1 = Label(win2 , text = "Enter your account number = ")
    amount = Label(win2 , text = "Enter amount to be deposited = ")
    b1 = Button(win2 , text = "DEPOSIT",command=DepoAmo)
    b1.place(x = 180 , y = 400)
    ano1.place(x = 50 , y = 180)
    amount.place(x = 50 , y = 240)
    global e1
    global e2
    e1 = Entry(win2)
    e1.place(x = 300 , y = 180)
    e2 = Entry(win2)
    e2.place(x = 300 , y = 240)
def DepoAmo():
    account1 = e1.get()
    am1 = int(e2.get());
    if(account1=="" or am1==""):
        MessageBox.showinfo("Deposit Status" , "All fields are required")
    else:
        c = con.cursor()
        a = "select Balance from Accounts where Account_no = %s"
        data = (account1,)
        c.execute(a,data)
        myresult = c.fetchone()
        tam = myresult[0] + am1
        sql = "update Accounts set Balance = %s where Account_no  = %s"
        d = (tam,account1)
        c.execute(sql,d)
        con.commit()
        MessageBox.showinfo("Deposit Status" , "Your amount has to be been deposited to your account!")
        con.close();
        
def WithdrawAmount():
    win3 = Tk()
    win3.title("Withdraw Amount")
    win3.geometry("500x600")
    ano1 = Label(win3 , text = "Enter your account number : ")
    amount = Label(win3 , text = "Enter amount to be withdrawn : ")
    b1 = Button(win3 , text = "Withdraw Amount",command=WithAmo)
    b1.place(x=180 ,y = 400)
    ano1.place(x = 50 , y =  180)
    amount.place(x = 50 , y = 240)
    global n1
    global n2
    n1 = Entry(win3)
    n1.place(x = 300 , y = 180)
    n2 = Entry(win3)
    n2.place(x = 300 , y = 240)

def WithAmo():
    account1 = n1.get()
    am1 = int(n2.get());
    if(account1=="" or am1==""):
        MessageBox.showinfo("Withdrawal Status" , "All fields are required")
    else:
        c = con.cursor()
        a = "select Balance from Accounts where Account_no = %s"
        data = (account1,)
        c.execute(a,data)
        myresult = c.fetchone()
        tam = myresult[0] - am1
        sql = "update Accounts set Balance = %s where Account_no = %s"
        d = (tam,account1)
        c.execute(sql,d)
        con.commit()
        MessageBox.showinfo("Withdrawal Status" , "Your amount is successfully withdrawed!")
        con.close();
        
def DisplayDetails():
    win4 = Tk()
    win4.title("Display Details")
    win4.geometry("400x300")
    cid = Label(win4 , text = "Enter your customer id : ")
    b1 = Button(win4 , text = "DISPLAY",command=dispcust)
    cid.place(x = 50 , y = 60)
    b1.place(x = 120 , y = 200)
    global a1
    a1 = Entry(win4)
    a1.place(x = 200 , y =  60)

def dispcust():
    win5 = Tk()
    win5.title("Your Customer Deatils")
    win5.geometry("500x600")
    cid1 = a1.get();
    data=cid1
    c = con.cursor()
    sql = "select * from Customer limit 0,10"
    c.execute(sql,data)
    i=0
    for Customer in c:
        for j in range(len(Customer)):
            e = Entry(win5 , width=10)
            e.grid(row=i,column=j)
            e.insert(END,Customer[j])
        i=i+1
    win5.mainloop()

def DeleteAccount():
    win6 = Tk()
    win6.title("Delete Account")
    win6.geometry("500x600")
    d1 = Label(win6 , text  =  "Enter your Customer ID: ")
    d2 = Label(win6 , text = "Enter your Account number : ")
    b1 = Button(win6 , text = "Delete",command=Del)
    d1.place(x = 50 , y = 180)
    d2.place(x = 50 , y = 270)
    b1.place(x = 180 , y = 400)
    global f1
    global f2
    f1 = Entry(win6)
    f1.place(x = 300 , y = 180)
    f2 = Entry(win6)
    f2.place(x = 300 , y = 270)
    
def Del():
    ano1 = f2.get();
    sql2 = "delete from Accounts where Account_no = '%s'" %ano1
    data2=ano1
    c = con.cursor()
    c.execute(sql2,data2)
    con.commit()
    MessageBox.showinfo("Delete Account" , "Your account has been succesffully deleted!")
    
window = Tk()
window.title("Bank Management System")
window.geometry("500x700")
window.configure(bg="Turquoise")
button1 = Button(window , text = "Open A New Account",font=("bold",12),command=OpenAccount)
button2 = Button(window , text = "Display Customer Details",font=("bold",12),command=DisplayDetails)
button3 = Button(window , text = "Withdraw Amount",font=("bold",12),command=WithdrawAmount)
button4 = Button(window , text = "Deposit Amount",font=("bold",12),command=DepositAmount)
button5 = Button(window , text = "Close An Account",font=("bold",12),command=DeleteAccount)
button6 = Button(window , text = "Balance Enquiry",font=("bold",10))
button1.place(x = 100 , y = 180)
button2.place(x = 100 , y = 360)
button3.place(x = 100 , y = 540)
button4.place(x = 300 , y = 180)
button5.place(x = 300 , y = 360)
button6.place(x = 300 , y = 540)
window.mainloop()
    


        
        
