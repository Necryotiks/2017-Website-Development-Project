import _io
from Records import Record
import threading
import importlib
import csv

test_record = Record() #initalize Record object
test_record.name = "Elliott Villars"  #set name
test_record.phone_num = "360-473-3137"
test_record.email = "eman13vil@gmail.com"
test_record.address = "9260 Ramiller LN SE"
test_record.city = "Port Orchard"
test_record.state = "WA"
test_record.zip = "98367"
test_record.carrier = "AT&T"
test_record.text = "THIS IS A TEST RECORD"
with open("Record_List.csv",'w+') as FileOBJ:
        CSVWriter = csv.writer(FileOBJ,delimiter = ',') # currently seperates each letter(FIXED)
        CSVWriter.writerow((test_record.name,test_record.phone_num,test_record.email,test_record.address,test_record.city,test_record.state,test_record.zip,test_record.carrier,test_record.text)) #need to figure out how to write the whole record


