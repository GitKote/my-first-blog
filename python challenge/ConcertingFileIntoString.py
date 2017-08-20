""" This python file helps us to convert the file data into a string"""

def fileIntoString(): 

	fileobject=open("pythonchallenge3.txt","r")
	for line in fileobject:
		line=line+" "
		print ("first line is ---- \n ",line)


fileIntoString()