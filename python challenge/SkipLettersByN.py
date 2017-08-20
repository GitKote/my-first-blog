import os;
import string;

os.system ('CLS')
"""
 This script will help to succeed the given alphabets by two steps 
example if a is given then it will print c like that

"""
def SkipLettersByN(customer_input,positions_to_skip): 


	customer_input=str(customer_input)
	positions_to_skip=int(positions_to_skip)


	print ("welcome to the script")

	alphabets=string.ascii_lowercase;

	print ("\n",alphabets);

	skipped_by_positioN={}
	#N=positions_to_skip
	for i in customer_input:
		if 
		new_index= customer_input.index(i) + positions_to_skip
		if ( new_index > len(customer_input) - 1  ):
			new_index = new_index-len(customer_input)
			print (new_index)
		skipped_by_positioN[i]=customer_input[new_index]
		print (skipped_by_positioN)
	return (skipped_by_positioN) 

print (SkipLettersByN("bottu seenu madatesi kodithey",1))

