import sys
from rooms import room_menu
from customers import customer_menu
from myprint import print_center, input_center
from database import get_database
if __name__ == '__main__':
    database, cursor = get_database()
    if database is None:
        print("The Database does not exist or not accessible.")
        sys.exit(1)
    while True:
        print()
        print_center("==============================")
        print_center("=====Apka Guruji Hotels=====")
        print_center("==============================")
        print_center("1. Manage Rooms")
        print_center("2. Manage Customers")
        print_center("0. Exit")
        print()
        choice = int(input_center("Enter your choice: "))
        if choice == 1:
            room_menu(database, cursor)
        elif choice == 2:
            customer_menu(database, cursor)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to exit)")
    print_center("GoodBye")
