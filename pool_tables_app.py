#1 create and array or dictionary with all 12 tables
# 2 should be able to see the list of tables and see occupied or not occupied
# 3 if the table is occupied then show the start time of the table (num of mins played)
# 4 if the pool table is occupied and you try to assign it the app prints "Pool table 8 is currently occupied"
# 5 When a table is returned create an entry into a text/JSON file
# 6 You need to retrieve the time

import datetime
import json
import pickle

poolTableList = []


class PoolTable:

    def __init__(self, number, status="UNOCCUPIED"):
        self.number = number
        self.status = status

    def table_status(self):
        if self.status == "OCCUPIED":
            print(f"Table {self.number} is occupied")


    def checkout(self):
        if self.status == "UNOCCUPIED":
            self.status == "OCCUPIED"
        self.start_time = datetime.datetime.now().replace(microsecond = 0)
        print(self.start_time)


    def checkin(self):
        if self.status == "OCCUPIED":
            self.status ==  "UNOCCUPIED"
        self.end_time = datetime.datetime.now().replace(microsecond = 0)
        print(self.end_time)
        self.total_time = (self.end_time - self.start_time)
        print(self.total_time)

    def print_reciept(self):
        file_time = str(datetime.datetime.now().strftime("%m-%d-%y"))
        #with open('filetime.txt', 'wb') as file:
            #print(self.__dict__)
            #file.write(json.dumps(self.__dict__))
        filename = file_time + ".txt"
        outfile = open(filename,'wb')
        pickle.dump(self, outfile)
        outfile.close()

        #pulls python data from text file
        infile = open(filename,'rb')
        new_dict = pickle.load(infile)
        print(new_dict, "this is python we loaded")
        infile.close()
    def __repr__(self):
        return(f"{self.total_time} {self.end_time} This is an object")

poolTableList = [PoolTable(1, 'UNOCCUPIED') for index in range(0, 12)]

choice = int(input('Enter table number to check out: '))

pool_table = poolTableList[choice-1]

pool_table.table_status()
pool_table.checkout()
pool_table.checkin()
pool_table.print_reciept()



# for table in poolTableList:
#     print(table.status)
#     print(table.number)
