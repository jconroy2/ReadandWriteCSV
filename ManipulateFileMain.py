import csv
import os
import commonFunctions

def readFileInputs(userFileName):
	print("Internal function")

def newFile(userFileName, matchingLines):
	print("Internal function")

def numOfMatches(userMatch, fileData):
	"""Find the number of word matches in the CSV file"""
	totalMatches = 0

	# if the word matches the user, increment totalMatches by 1
	for row in fileData:
		for word in row:
			if word == userMatch:
				totalMatches += 1
	return totalMatches

def numOfLines(userMatch, fileData):
	"""Find the number of lines that have the word in the CSV file"""
	totalLines = 0

	# if the users word is in any row, increment totalLines by 1
	for row in fileData:
		if any(userMatch in cell for cell in row):
			totalLines += 1
	return totalLines

def eachMatchingLine(userMatch, fileData):
	"""Put each line that matches into an array"""
	matchingLines = []

	# if the user word is in a row, append that whole line into matchingLines
	for row in fileData:
		if any(userMatch in cell for cell in row):
			matchingLines.append(row)
	return matchingLines

if __name__ == "__main__":

	"""Get user input for what word they need to match"""
	userMatch = input("What word are you looking for to match? ")
	userFileName = input("What is the file ou want to import? ")

	fileData = commonFunctions.readFileInputs(userFileName)

	totalMatches = numOfMatches(userMatch, fileData)
	print("The total number of matches is ", totalMatches)

	totalLines = numOfLines(userMatch, fileData)
	print("The total number of lines that has the matching word is ", totalLines)

	matchingLines = eachMatchingLine(userMatch, fileData)
	if matchingLines:
		newFileName = commonFunctions.newFile(userFileName, matchingLines)
		print("The new file name is ", newFileName)
	else:
		print("No lines match, a new file will not be created")
