import sys
import re
import read_file

def enough_info():
	'''Find out what kind of data are present in the file 
	(ie 3k, 9k, 19k or 26k)'''
	file = read_file.get_fname()
	kage = re.findall(r'\d|\d\d', file)
	kage = kage[0]
	if len(kage) == 0:
		kage = raw_input("The file name does not say how many SNPs are in this \
					      file. Please enter the number of thousands of \
						  SNPs in file (if your data is '3k' SNP data, for \
						  for example, enter '3' ")	
	return(kage)



if __name__ == '__main__':
    enough_info()



