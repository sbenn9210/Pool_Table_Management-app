#1 create and array or dictionary with all 12 tables
# 2 should be able to see the list of tables and see occupied or not occupied
# 3 if the table is occupied then show the start time of the table (num of mins played)
# 4 if the pool table is occupied and you try to assign it the app prints "Pool table 8 is currently occupied"
# 5 When a table is returned create an entry into a text/JSON file
# 6 You need to retrieve the time

import datetime
import json
import pickle




class PoolTable:

    def __init__(self, number, status="UNOCCUPIED"):
        self.number = number
        self.status = status
        self.total_time = None
        self.end_time = None

    def table_status(self):
        if self.status == "OCCUPIED":
            print(f"Table {self.number} is occupied")


    def checkout(self):
        if self.status == "UNOCCUPIED":
            self.status = "OCCUPIED"
        self.start_time = datetime.datetime.now().replace(microsecond = 0)
        print(self.start_time)


    def checkin(self):
        if self.status == "OCCUPIED":
            self.status =  "UNOCCUPIED"
        self.end_time = datetime.datetime.now().replace(microsecond = 0)
        print(self.end_time)
        self.total_time = (self.end_time - self.start_time)
        print(self.total_time)
        self.cost = self.total_time * .5
        print("$", self.cost)

    def print_reciept(self):
        file_time = str(datetime.datetime.now().strftime("%m-%d-%y"))
        self.endtime = str(self.end_time)
        print(file_time)

        the_data = {
            'Start time': str(self.start_time),
            'End time': str(self.end_time),
            'Total time': str(self.total_time),
            'Cost': str(self.cost)
        }

        with open('filetime.txt', 'w') as file:
            print(self.__dict__)
            file.write(json.dumps(the_data))

    def __repr__(self):
        return(f"{self.number} {self.status}")




