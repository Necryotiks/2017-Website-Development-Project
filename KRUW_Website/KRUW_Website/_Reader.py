import csv
from Records import Record
def recordReader(recordArray):
    with open("Record_List.csv",'r') as FileOBJ:#reads in from file
        CSVReader = csv.reader(FileOBJ)
        for row in CSVReader:
            x = Record()
            #
            #add shit to each record instance here
            #
            x.add_Name(row[0])
            x.add_Phone(row[1])
            x.add_Email(row[2])
            x.add_Street_Address(row[3])
            x.add_City(row[4])
            x.add_State(row[5])
            x.add_ZIP(row[6])
            x.add_Carrier(row[7])
            x.add_Textblock(row[8])
            recordArray.append(x)
        FileOBJ.close()
    return