from datetime import datetime

from myprint import print_bar

TABLE_NAME = "customers"


class Customer:
    def __init__(self):
        self.customer_id = 0
        self.name = ""
        self.address = ""
        self.phone = ""
        self.room_no = "0"
        self.entry_date = ""
        self.checkout_date = ""

    def create(self, customer_id, name, address, phone, room_no, entry_date, checkout_date):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.room_no = room_no
        self.entry_date = entry_date
        self.checkout_date = checkout_date
        return self

    def create_from_record(self, record):
        self.customer_id = record['id']
        self.name = record['name']
        self.address = record['address']
        self.phone = record['phone']
        self.room_no = record['room_no']
        self.entry_date = record['entry']
        self.checkout_date = record['checkout']
        return self

    def print_all(self):
        print(str(self.customer_id).ljust(3),
              self.name[0:15].ljust(15),
              self.address[0:15].ljust(15),
              self.phone.ljust(15),
              str(self.room_no).ljust(10),
              self.entry_date.strftime("%d-%b-%y").ljust(15),
              (self.checkout_date.strftime("%d %b %y") if self.checkout_date is not None else "None").ljust(15))

    def print_full(self):
        print_bar()
        print("Customer #", self.customer_id)
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Phone: ", self.phone)
        print("Checked in to room #", self.room_no, " on ", self.entry_date.strftime("%d %b %y"))
        print("Checkout: ", self.checkout_date.strftime("%d %b %y") if self.checkout_date is not None else None)
        print_bar()


def create_customer(room_no):
    customer_id = None
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = input("Enter the phone: ")
    entry_date = datetime.now()
    return Customer().create(customer_id, name, address, phone, room_no, entry_date, None)


def print_header():
    print("="*100)
    print("id".ljust(3),
          "name".ljust(15),
          "address".ljust(15),
          "phone".ljust(15),
          "room no".ljust(10),
          "entry".ljust(15),
          "check out".ljust(15))
    print("="*100)


def create_table(database):
    cursor = database.cursor()
    cursor.execute("DROP table if exists {0}".format(TABLE_NAME))
    cursor.execute("create table {0} ("
                   "id int primary key auto_increment,"
                   "name varchar(20),"
                   "address varchar(50),"
                   "phone varchar(10),"
                   "room_no int,"
                   "entry datetime,"
                   "checkout datetime)".format(TABLE_NAME))

