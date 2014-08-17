import pandas as pd
import sys
import csv
import re

def read_file():
	'''Read in file containing genomic data. Done this way because Pandas is 
	fast and easy to use, but has difficulty with ragged arrays.'''
	lines=list(csv.reader(open(sys.argv[1])))
#lines=list(csv.reader(open('CTL 3K 06jul2011_LocusXDNA.csv')))
	df =pd.DataFrame(lines)
	return(df)

if __name__ == '__main__':
    read_file()

