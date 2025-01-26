import csv
import os

def readFileInputs(userFileName):
	"""Read the CSV file contents"""
	try:
		with open(userFileName, 'r') as csvfile:
			print("Successfully opened the given file")
			csv_reader = csv.reader(csvfile)
			data = []
			for row in csv_reader:
				data.append(row)
			return data
	except FileNotFoundError:
		print("Error: The file ", userFileName, " does not exist. Please check the file name and try again.")
		exit()

def newFile(userFileName, matchingLines):
	"""Create a new file with the matching lines"""
	baseName, extension = os.path.splitext(userFileName)
	newFileName = f"{baseName}_update{extension}"

	#creates a new csv file and adds the lines that had the user match
	with open(newFileName, mode='w', newline='', encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(matchingLines)
	return newFileName
