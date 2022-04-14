import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="12345678",database="Bank")

def openAccount():
    name = input("Enter your Name : ")
    account_no = input("Enter your Account number : ")
    dob = input("Enter your Date Of Birth(DD/MM/YYYY) : ")
    phone_no = input("Enter your phone number(10 digits) : ")
    address = input("Enter your address : ")
    opening_bal = int(input("Enter Opening Balance Amount : "))
    data1 = (name,account_no,dob,phone_no,address,opening_bal)
    data2 = (name,account_no,opening_bal)
    sql1 = "insert into Account values(%s,%s,%s,%s,%s,%s)"
    sql2 = "insert into Amount values(%s,%s,%s)"
    c = con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("Data Entered Successfully")
    main()

def depositAmount():
    amount = int(input("Enter Amount to be deposited : "))
    account_no = input("Enter Account number : ")
    a = "select Balance from Amount where account_no = %s"
    data = (account_no,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    tam = myresult[0] + amount
    sql = "update Amount set Balance = %s where account_no = %s"
    d = (tam,account_no)
    c.execute(sql,d)
    con.commit()
    print("Amount successfully deposited")
    main()

def withdrawAmount():
    amount = int(input("Enter Amount to be withdrawn : "))
    account_no = input("Enter Account number : ")
    a = "select Balance from Amount where account_no = %s"
    data = (account_no,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    tam = myresult[0] - amount
    sql = "update Amount set Balance = %s where account_no = %s"
    d = (tam,account_no)
    c.execute(sql,d)
    con.commit()
    print("Amount successfully withdrawn")
    main()

def Balance():
    account_no = input("Enter Account number : ")
    a = "select Balance from Amount where account_no = %s"
    data = (account_no,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    print("Balance for Account : ",account_no," is ",myresult[0])
    main()

def displayAccount():
    account_no = input("Enter Account number : ")
    a = "select * from Account where account_no = %s"
    data = (account_no,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    for i in myresult:
        print(i,end = " ")
    main()

def closeAccount():
    account_no = input("Enter Account number : ")
    sql1 = "delete from Account where account_no = %s"
    sql2 = "delete from Amount where account_no = %s"
    data = (account_no,)
    c = con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    print("Account has been successfully deleted")
    main()

def main():
    print("""
          1. OPEN NEW ACCOUNT
          2. DEPOSIT AMOUNT
          3. WITHDRAW AMOUNT
          4. BALANCE ENQUIRY
          5. DISPLAY CUSTOMER DETAILS
          6. CLOSE AN ACCOUNT
          """)
    choice = input("Enter task number = ")
    if(choice == "1"):
        openAccount()
    elif(choice == "2"):
        depositAmount()
    elif(choice == "3"):
        withdrawAmount()
    elif(choice == "4"):
        Balance()
    elif(choice == "5"):
        displayAccount()
    elif(choice == "6"):
        closeAccount()
    else:
        print("Wrong Choice.........")
        main()
main()
