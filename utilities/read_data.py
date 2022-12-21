import csv


def getCSVdata(fileName):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    dataFile= open(fileName, 'r')
    # create a CSV reader frin the CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows to the reader list
    for row in reader:
        rows.append(row)
    return rows

