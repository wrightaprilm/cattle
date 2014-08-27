import argparse
import getopt
import sys
from Tkinter import Tk
from tkFileDialog import askopenfilename

def main():
	Tk().withdraw() 
	filename = askopenfilename()

	'''main function to collate the args'''
	'''try:                               
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["infile=","ofile="]) 
	except getopt.GetoptError:           
		print 'Please specify a file'                         
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--infile"):
			inputfile = arg
			print 'Input file is "', inputfile
		elif opt in ("-o", "--ofile"):
			outputfile = arg
#			print 'Output file is "', outputfile'''
	return(filename)

if __name__ == '__main__':
    main()
