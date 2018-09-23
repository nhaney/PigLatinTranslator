#! /usr/bin/python

import re #regex used for my function to split up the line
import sys
import os
from igpay import igpay

def stringToList(string):
	'''removes spaces and then seperates characters and symbols in a
	list of lists'''
	#first split by spaces
	newStrings = string.split()
	#then we will further split this by seperating characters and symbols
	for index,word in enumerate(newStrings):
		newStrings[index] = re.findall(r"[\w]+|[^\s\w]", word)
	#returns a list of lists
	return newStrings

def translateToPigLatin(filename):
	'''translates all words in file to pig latin and outputs to
	std output'''
	for line in open(filename):
		#we have to delimit spaces and punctuation
		words = stringToList(line)
		#loop through the words that we got and igpay them
		tempLine = ""
		for w in words:
			tempString = ""
			for elem in w:
				tempString += igpay(elem)
			tempLine += tempString + " "
		print(tempLine)

def main():
	if(len(sys.argv) >= 2):
		#make sure the file exists 
		try:
      		        open(sys.argv[1], "r")
		except IOError:
			print("Error: file %s does not exist!" % sys.argv[1])
			return

		#if you want an output file (automatically igpays the name)
		if(len(sys.argv) >= 3):
			if(sys.argv[2] == "1"):
				newFileName = sys.argv[1].split(".") #splits at file extension
				newFileName = igpay(newFileName[0]) + ".txt"
				print("Program is outputting to: %s..." % newFileName)
				sys.stdout = open(newFileName, "w+")
		translateToPigLatin(sys.argv[1])
	else:
		print("Please enter a filename to translate.")
		print("Format: $ ./atinlay [filename] {1}; See readme.txt (or eadmeray.txt, if fluent) for more information.")

if __name__ == '__main__':
	main()












