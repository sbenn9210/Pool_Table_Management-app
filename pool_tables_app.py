#1 create and array or dictionary with all 12 tables
# 2 should be able to see the list of tables and see occupied or not occupied
# 3 if the table is occupied then show the start time of the table (num of mins played)
# 4 if the pool table is occupied and you try to assign it the app prints "Pool table 8 is currently occupied"
# 5 When a table is returned create an entry into a text/JSON file
# 6 You need to retrieve the time

import time


poolTableList = []


class PoolTable:

    def __init__(self, number, status="UNOCCUPIED"):
        self.number = number
        self.status = status

    def table_status(self, status):
        if status == "OCCUPIED":
            print(f"Table {self.number} is occupied")
            

    def checkout(self):
        self.status = "OCCUPIED"
        self.start_time = time.strftime("%m-%d-%Y %I:%M")
        print(self.start_time)


    def checkin(self):
        self.status =  "UNOCCUPIED"
        self.end_time = time.strftime("%m-%d-%Y %I:%M")
        print(self.end_time)




poolTableList = [PoolTable(1, 'UNOCCUPIED') for index in range(0, 12)]

choice = int(input('Enter table number to check out: '))

pool_table = poolTableList[choice-1]
pool_table.checkout()
pool_table.number = 999



print(poolTableList[0].status)
print(poolTableList[0].number)
