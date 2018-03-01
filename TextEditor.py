import os
import sys
import shutil
def write():
	try:
		filename = raw_input("Enter filename")
		target = open(filename, "a");
		while True:
			data = raw_input()
			if (data.lower() == "exit"):
				break
			target.write(data)
			target.write("\n")
	except Exception as e:
		print "Oops, there was a problem" + e
def read():
	try:
		filename = raw_input("Enter filename")
		target = open(filename, "r")
		readData = target.read()
		print readData
	except Exception as e:
		print "Oops, there was a problem" + e
def exit():
	sys.exit("You are leaving awesome editor! Byee! :)")
def rename():
	try:
		filename = raw_input("Enter filename")
		newName = raw_input("New filename")
		shutil.move(filename, newName)
	except Exception as e:
		print "Oops, there was a problem" + e
def delete():
	try: 
		filename = raw_input("Enter filename")
		os.unlink(filename)
	except Exception as e:
		print "Oops, there was a problem" + e

if __name__ == "__main__" :
	print "Option write, read, exit, delete, rename"
	input = raw_input("So, what are you wishing to do? ")
	if(input.lower() == "write"):
		write()
	elif(input.lower() == "read") :
		read()
	elif(input.lower() == "exit"):
		exit()
	elif(input.lower() == "rename"):
		rename()
	elif(input.lower() == "delete"):
		delete()

