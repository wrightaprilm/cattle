import pandas
with open('test.csv') as f:
	lines = [line.strip().split(',') for line in f]

data_row = [line for line in lines if line[1] == 'snps' or 'SNPS']



print lines
