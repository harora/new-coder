from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

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

def visualize_days():
	"""visualize days of week """
	data_file = parse(MY_FILE, ",")

	counter = Counter(item["Resolution"] for item in data_file)

	data_list = [
				counter["ARREST, BOOKED"],
				counter["ARREST, CITED"],
				counter["NONE"],
				counter["JUVENILE BOOKED"]				
				]

	reso_tuple = tuple(["Ab","Ac","None","Juv","Fri","Sat","Sun"])

	plt.plot(data_list)

	plt.xticks(range(len(reso_tuple)),reso_tuple)

	plt.savefig("Resolution.png")

	plt.clf()



def visualize_type():
    """Visualize data by category in a bar graph"""
    data_file = parse(MY_FILE, ",")
    # Same as before, this returns a dict where it sums the total
    # incidents per Category.
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter.
    labels = tuple(counter.keys())

    # Set where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the graph!
    # If you look at new-coder/dataviz/tutorial_source, you should see
    # the PNG file, "Type.png".  This is our graph!
    plt.savefig("Type.png")

    # Close figure
    plt.clf()









def main():
	visualize_days()
	visualize_type()


if __name__ == "__main__":
	main()
