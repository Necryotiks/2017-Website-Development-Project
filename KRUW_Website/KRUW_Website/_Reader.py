import csv
from Records import Record
def recordReader(recordArray):
    with open("Record_List.csv",'r') as FileOBJ:#reads in from file
        CSVReader = csv.reader(FileOBJ)
        for row in CSVReader:
            x = Record()
            #
            #add shit to record here
            #
            recordArray.append(x)
        FileOBJ.close()
    return