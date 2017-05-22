import csv
#from Records import Record

def recordWriter(recordArray):
    with open("Record_List.csv",'w') as FileOBJ:
        CSVWriter = csv.writer(FileOBJ)
        for line in recordArray: #BROKE
            CSVWriter.writerow((line.name,line.phone_num,line.email,line.address,line.city,line.state,line.zip,line.carrier,line.text))#finish
        return