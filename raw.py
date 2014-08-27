import pandas
import csv

inputfile = raw_input("Hi Debbie, what file would you like to parse:" )

lines=list(csv.reader(open(inputfile)))

print lines
