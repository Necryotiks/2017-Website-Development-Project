import _io
import threading

class Record:
	def __init__(self):#Initialize the object
		self._x = _x
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

try:
	open("Record_List",'a')
except IOError:
	open("Record_List",'x')

