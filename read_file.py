import pandas as pd
import sys
import csv
import integrate

def read_file(file):
	'''Read in file containing genomic data. Done this way because Pandas is 
	fast and easy to use, but has difficulty with ragged arrays.'''
	lines=list(csv.reader(open(file)))
	df =pd.DataFrame(lines)
	return(df)

if __name__ == '__main__':
	read_file(file)


