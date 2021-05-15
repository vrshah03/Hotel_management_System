from datetime import datetime

import mysql

from customer import Customer, create_customer, TABLE_NAME, create_table, print_header
from rooms import get_and_print_room_by_no, change_room_status
NUMBER_OF_RECORDS_PER_PAGE = 10


def add_customer(database, cursor):
    room = get_and_print_room_by_no(cursor)
    if room is not None:
        customer = create_customer(room.room_no)
        confirm = input("Complete the operation? (Y/N) ").lower()
        if confirm == 'y':
            query = "insert into {0}(name, address, phone, room_no, entry) values('{1}','{2}','{3}',{4},'{5}')". \
                format(TABLE_NAME, customer.name, customer.address, customer.phone,
                       customer.room_no, customer.entry_date.strftime("%Y-%m-%d %H:%M:%S"))
            try:
                cursor.execute(query)
                database.commit()
            except mysql.connector.Error:
                create_table(database)
                cursor.execute(query)
                database.commit()
            change_room_status(database, cursor, room.room_id, False)
            print("Operation Successful")
        else:
            print("Operation Canceled")


def show_records(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        print_header()
        for record in records:
            customer = Customer().create_from_record(record)
            customer.print_all()
        return records
    except mysql.connector.Error as err:
        print(err)


def show_record(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        record = records[0]
        customer = Customer().create_from_record(record)
        customer.print_full()
        return customer
    except mysql.connector.Error as err:
        print(err)


def get_and_print_customer_by_room_no(cursor):
    room = get_and_print_room_by_no(cursor)
    if room is not None:
        query = "select * from {0} where room_no={1} order by id desc limit 1".format(TABLE_NAME, room.room_no)
        customer = show_record(cursor, query)
        return room, customer
    return None, None


def check_out(database, cursor):
    room, customer = get_and_print_customer_by_room_no(cursor)
    if room is not None and customer is not None:
        confirm = input("Confirm checkout? (Y/N): ")
        if confirm == 'y':
            checkout = datetime.now()
            query = "update {0} set checkout='{1}' where id={2}".\
                format(TABLE_NAME, checkout.strftime("%Y-%m-%d %H:%M:%S"), customer.customer_id)
            cursor.execute(query)
            database.commit()
            change_room_status(database, cursor,room.room_id, True)
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def edit_by_room_no(database, cursor):
    room, customer = get_and_print_customer_by_room_no(cursor)
    if room is not None and customer is not None:
        query = "update {0} set".format(TABLE_NAME)
        print("Input new values (leave blank to keep previous value)")
        name = input("Enter new name: ")
        if len(name) > 0:
            query += " name='{0}',".format(name)
        address = input("Enter new address: ")
        if len(address) > 0:
            query += " address='{0}',".format(address)
        phone = input("Enter number of phone: ")
        if len(phone) > 0:
            query += " phone='{0}',".format(phone)
        query = query[0:-1] + " where id={0}".format(customer.customer_id)
        confirm = input("Confirm Update (Y/N): ").lower()
        if confirm == 'y':
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def delete_by_room_no(database, cursor):
    room, customer = get_and_print_customer_by_room_no(cursor)
    if room is not None and customer is not None:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where id={1}".format(TABLE_NAME, customer.customer_id)
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")

def customer_menu(database, cursor):
    while True:
        print()
        print("==============================")
        print("==========Customer Menu=========")
        print("==============================")
        print()
        print("1. New Customer")
        print("2. Show Customer Details by name")
        print("3. Show customer details by customer_id")
        print("4. Show customer details by address")
        print("5. Show customer details by phone number")
        print("6. Show customer details by room no")
        print("7. Show customer details by check in date")
        print("8. Show current list of customers")
        print("9. Check out")
        print("10. Edit customer Details")
        print("11. Delete Customer record")
        print("12. View all customers")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_customer(database, cursor)
        elif choice == 2:
            name = input("Enter the name: ").lower()
            query = "select * from {0} where name like '%{1}%'".format(TABLE_NAME, name)
            show_records(cursor, query)
        elif choice == 3:
            customer_id = input("Enter the customer id: ")
            query = "select * from {0} where id = {1}".format(TABLE_NAME, customer_id)
            show_record(cursor, query)
        elif choice == 4:
            address = input("Enter the address: ").lower()
            query = "select * from {0} where address like '%{1}%'".format(TABLE_NAME, address)
            show_records(cursor, query)
        elif choice == 5:
            phone = input("Enter the phone number: ")
            query = "select * from {0} where phone like '%{1}%'".format(TABLE_NAME, phone)
            show_records(cursor, query)
        elif choice == 6:
            room_no = input("Enter the room_no: ")
            query = "select * from {0} where room_no = {1}".format(TABLE_NAME, room_no)
            show_record(cursor, query)
        elif choice == 7:
            print("Enter the check in date: ")
            day = int(input("day of month: "))
            month = int(input("month: "))
            year = int(input("year: "))
            query = "select * from {0} where date(entry) = '{1}-{2}-{3}'".format(TABLE_NAME, year, month, day)
            show_records(cursor, query)
        elif choice == 8:
            query = "select * from {0} where checkout is null".format(TABLE_NAME)
            show_records(cursor, query)
        elif choice == 9:
            check_out(database, cursor)
        elif choice == 10:
            edit_by_room_no(database, cursor)
        elif choice == 11:
            delete_by_room_no(database, cursor)
        elif choice == 12:
            query = "select * from {0}".format(TABLE_NAME)
            show_records(cursor, query)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
