class Record:
    name = None
    phone_num = None
    email = None
    address = None
    carrier = None
    text = None
def __init__(self):#Initialize the object; functions like a constructor 
    self.name = ""
    self.phone_num = ""
    self.email = ""
    self.address = ""
    self.carrier = ""
    self.text = ""
def add_Name(self,name): #First,Last name
		self.name = name
def add_Phone(self,phone_num):#phone number
		self.phone_num = phone_num
def add_Email(self,email):#email address
		self.email = email
def add_Address(self,address):#physical address
		self.address = address
def add_Carrier(self,carrier):#phone carrier
		self.carrier = carrier
def add_Textblock(self,text):#text for record
		self.text = text

