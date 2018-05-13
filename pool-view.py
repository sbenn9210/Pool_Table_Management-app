from pool_tables_app import *

poolTableList = []

poolTableList = [PoolTable(index, 'UNOCCUPIED') for index in range(1, 13)]

active = True
while active:

    print("\n************************************************************")
    print("Enter 1 to check out a table: ")
    print("-------------------------------------------------")
    print("Enter 2 to check in a table: ")
    print("-------------------------------------------------")
    print("Enter 3 to view all tables: ")
    print("-------------------------------------------------")
    print("Enter 4 to print print_reciept")
    print("-------------------------------------------------")
    print("Enter q to quit: ")
    print("************************************************************\n")

    choice = input("Enter choice: ")

    if choice == "q":
        active = False

    elif choice == "1":
        user_table_selection = int(input("Enter table number to checkout: "))
        table = poolTableList[user_table_selection - 1]
        print(table.status)
        if table.status == "OCCUPIED":
            table.table_status()

        else:
            table.checkout()

    elif choice == "2":
        user_table_selection = int(input("Enter table number to checkin: "))
        table = poolTableList[user_table_selection - 1]
        table.checkin()

    elif choice == "3":
        for table in poolTableList:
            print(table)


    elif choice == "4":
        table.print_reciept()