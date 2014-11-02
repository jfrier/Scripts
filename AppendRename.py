#!/usr/bin/python
import sys
import os
from os import listdir

print ("Number of arguments: " + str(len(sys.argv)))
print ("Argument List: " +  str(sys.argv))

if len(sys.argv) != 3:
	print("Invalid number of arguments")
	exit(1)

mypath = sys.argv[1]
print ("Path: " + mypath)
prefix = sys.argv[2]
print ("\n")

for filename in os.listdir(mypath):
	if os.path.isfile(os.path.join(mypath, filename)):
		# if (filename.startswith("n")):
			# os.rename(os.path.join(mypath, filename), os.path.join(mypath, filename[1:]))
		filenamepath = os.path.join(mypath, filename)
		print("Renaming: " + filenamepath)
		os.rename(filenamepath, os.path.join(mypath, prefix + filename))
