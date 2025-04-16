import os
import sys
import importlib

def parameter_input():
	inputPara=[]
	inputN=input("Input the numbers of parameters:  \n||a line of input count as one                                         ||\n||a list must input in one line and place a space between each elements||\n")
	for i in range(int(inputN)):
		inTem=input()
		if inTem.isdigit():
			inputPara.append(int(inTem))
		elif inTem.isalpha():
			inputPara.append(str(inTem))
		else:
			inTem2=inTem.split()
			if inTem2[0].isdigit():
				for j in range(len(inTem2)):
					inTem2[j]=int(inTem2[j])
			inputPara.append(inTem2)
	return inputPara

#main function
print("Put yout .py file in test_code folder.")
fileName = input("Input the filename in testing_code folder: ")
funName = input("Input the function name in your file: ")
fileName = fileName[:-3]
#print(f"filename : {fileName}")
try:
	module=importlib.import_module(f"testing_code.{fileName}")
	inputlist=[]
	if hasattr(module,funName):
		method=getattr(module,funName)
		inputlist=parameter_input()
		#print (inputlist)
		try:		
			re = method(*inputlist)
			print(re)
		except:
			print("Wrong input")
	else:
		print("Function not found")
except:
	print("File not found")
