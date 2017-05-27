import _io
import fileinput
import threading
import importlib
from _Reader import recordReader
from _Writer import recordWriter

recordArray = []

recordArray = recordReader(recordArray) #Reads form file. stores into record
#
#recordWriter(recordArray)#BROKE AS FUCK

#with open("Record_List.csv",'a') as FileOBJ:
#    CSVWriter = csv.writer(FileOBJ)
#    for row in recordArray:
       

