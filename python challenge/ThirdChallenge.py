
fileobject=open("pythonchallenge3.txt","r")
answer_dictionary={}
for line in fileobject:
	for letter in line:
		if letter in answer_dictionary:
			answer_dictionary[letter]=answer_dictionary[letter]+1
		else:
			answer_dictionary[letter]=0
fileobject.close();
print (answer_dictionary)
answer=""
for key,value in answer_dictionary.items():
	if value == 0 :
		answer=answer+key
		
print ("\n",answer)