import mysql.connector

global z
mydb = mysql.connector.connect(user='vatsal', password='root', host='localhost', database='hms')

mycursor = mydb.cursor()


def registercust():
    L = []
    custname = input("enter name:")
    L.append(custname)
    addr = input("enter address:")
    L.append(addr)
    indate = input("enter check in date:")
    L.append(indate)
    outdate = input("enter check out date:")
    L.append(outdate)
    cust = (L)
    sql = "insert into hms.custdata(custname,addr,indate,outdate)values(%s,%s,%s,%s)"
    mycursor.execute(sql, cust)
    mydb.commit()


'''def roomtypeview():
    print("Do yoy want to see room type available : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from hms.roomtype"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)'''


def roomrent():
    print("We have the following rooms for you:-")
    print("1. type A---->rs 1000 PN\-")
    print("2. type B---->rs 2000 PN\-")
    print("3. type C---->rs 3000 PN\-")
    print("4. type D---->rs 4000 PN\-")
    x = int(input("Enter Your Choice Please->"))
    n = int(input("For How Many Nights Do You want to Stay:"))
    if (x == 1):
        print("you have opted room type A")
        s = 1000 * n
    elif (x == 2):
        print("you have opted room type B")
        s = 2000 * n
    elif (x == 3):
        print("you have opted room type C")
        s = 3000 * n
    elif (x == 4):
        print("you have opted room type D")
        s = 4000 * n
    else:
        print("please choose a room")
    print("your room rent is =", s, "\n")


'''def restaurentmenuview():
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from hms.restaurent"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)'''


def orderitem():
    global s
    print("Do you want to see menu available : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from hms.restaurent"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)

    print('do you want to purchase from list:'
          '1-tea(Rs.10)-->2-coffee(Rs.10)-->3-coldrink(Rs.20)-->4-samosa(Rs.10)-->5-sandwich(Rs.50)-->6-dhokla(Rs.30)-->7-kachori(Rs.10)-->8-milk(Rs.20)-->9-noodles(Rs.50)-->10-pasta(Rs.50)')
    d = int(input("enter your choice:"))
    if (d == 1):
        print("you have ordered tea")
        a = int(input("enter quantity"))
        s = 10 * a
        print("your amount for tea is :", s, "\n")
    elif (d == 2):
        print("you have ordered coffee")
        a = int(input("enter quantity"))
        s = 10 * a
        print("your amount for coffee is :", s, "\n")
    elif (d == 3):
        print("you have ordered colddrink")
        a = int(input("enter quantity"))
        s = 20 * a
        print("your amount for colddrink is :", s, "\n")
    elif (d == 4):
        print("you have ordered samosa")
        a = int(input("enter quantity"))
        s = 10 * a
        print("your amount for samosa is :", s, "\n")
    elif (d == 5):
        print("you have ordered sandwich")
        a = int(input("enter quantity"))
        s = 50 * a
        print("your amount for sandwich is :", s, "\n")
    elif (d == 6):
        print("you have ordered dhokla")
        a = int(input("enter quantity"))
        s = 30 * a
        print("your amount for dhokla is :", s, "\n")
    elif (d == 7):
        print("you have ordered kachori")
        a = int(input("enter quantity"))
        s = 10 * a
        print("your amount for kachori is :", s, "\n")
    elif (d == 8):
        print("you have ordered milk")
        a = int(input("enter quantity"))
        s = 20 * a
        print("your amount for kachori is :", s, "\n")
    elif (d == 9):
        print("you have ordered noodles")
        a = int(input("enter quantity"))
        s = 50 * a
        print("your amount for noodles is :", s, "\n")
    elif (d == 10):
        print("you have ordered pasta")
        a = int(input("enter quantity"))
        s = 50 * a
        print("your amount for pasta is :", s, "\n")
    else:
        print("please enter your choice from the menu")


def laundarybill():
    global z
    print("Rate of laundry is Rs.10 : Enter 1 for confirm :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from hms.laundry"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)
    y = int(input("Enter Your number of clothes->"))
    z = y * 10
    print("your laundary bill:", z, "\n")
    return z


def lb():
    print(z)





def viewbill():
    a = input("enter customer name:")
    print("customer name :", a, "\n")
    print("laundary bill:",z,"\n")





def Menuset():
    print("==============================")
    print("=====TAJ SKYLINE Hotel=====")
    print("==============================")
    print("enter 1 : To enter customer data")
    #print("enter 2 : To view roomtype")
    print("enter 2 : for calculating room bill")
    #print("enter 4 : for viewing restaurent menu")
    print("enter 3 : for restaurent bill")
    print("enter 4 :for laundary bill")
    print("enter 5 : for customer name and laundary bill")
    print("enter 6 : for exit:")

    userinput = int(input("enter your choice:"))
    if (userinput == 1):
        registercust()
    #elif (userinput == 2):
        #roomtypeview()
    elif (userinput == 2):
        roomrent()
    #elif (userinput == 4):
        #restaurentmenuview()
    elif (userinput == 3):
        orderitem()
    elif (userinput == 4):
        laundarybill()
    elif (userinput == 5):
        viewbill()
    elif (userinput == 6):
        quit()
    else:
        print("enter correct choice:")


Menuset()


def runagain():
    runagn = input("\n want to run again y/n:")
    while runagn.lower() == 'y':

        Menuset()


runagain()
