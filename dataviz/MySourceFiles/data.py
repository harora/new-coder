import csv

MY_FILE = "/home/himanshu/new-coder/dataviz/sample_sfpd_incident_all.csv"

def parse(raw_file,delimiter):
	""" Parses a raw CSV file to a JSON-line object """
    #open CSV file
	opened_file = open(raw_file)

	#Read the CSV data
	csv_data = csv.reader(opened_file, delimiter = delimiter)

	#setup an empty list
	parsed_data = []

	#skip over the first line of the file for the headers
	fields = csv_data.next()

	#Iterate over each row of the csv file , zip together field -> value
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	#close the csv file 
	opened_file.close()

    #close the CSV file
	return parsed_data

def main():
	#call our parse function and give it needed parameters
	new_data = parse(MY_FILE, ",")

	print new_data


if __name__ == "__main__":
	main()