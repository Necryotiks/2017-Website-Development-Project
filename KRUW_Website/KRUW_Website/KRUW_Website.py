import _io
from Records import Record
import threading
import importlib
import csv

test_record = Record() #initalize Record object
test_record.name = "Elliott"  #set name

with open("Record_List.csv",'a+') as FileOBJ:
        CSVWriter = csv.writer(FileOBJ,delimiter = ',') # currently seperates each letter(FIXED)
        CSVWriter.writerow([test_record.name]);


