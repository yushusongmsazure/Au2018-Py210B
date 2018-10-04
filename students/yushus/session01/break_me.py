import sys

def yushus_Exception_NameError():
	try:
		raise NameError	
	except NameError:
		print("Catched NameError")

def yushus_Exception_TypeError():
	try:
		raise TypeError
	except TypeError:
		print("Catched TypeError")
	
def yushus_Exception_SyntaxError():
	try:
		with open('file.log') as file:
			read_data = file.read()
	except FileNotFoundError as fnf_error:
		print(fnf_error)	
		
def yushus_Exception_AttributeError():
	try:
		raise AttributeError
	except AttributeError:
		print("Catched AttributeError")
	
#yushus_Exception_NameError()
#yushus_Exception_TypeError()
yushus_Exception_SyntaxError()
#yushus_Exception_AttributeError()