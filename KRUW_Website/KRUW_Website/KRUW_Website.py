import _io
import fileinput
from Records import Record
import threading
import importlib
from _Reader import recordReader

recordArray = []

recordArray = recordReader(recordArray) #Reads form file. stores into record

#with open("Record_List.csv",'a') as FileOBJ:
#    CSVWriter = csv.writer(FileOBJ)
#    for row in recordArray:
       

