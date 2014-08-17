import pandas as pd
import parse_prop
import add_seq

def append():
	'''We want to store the raw data without the append and merge. So now we do 
	the append and merge'''
	just_snps = add_seq.add_sequences()
	print just_snps
	second_df = just_snps
	replaced = just_snps.replace({'A':0,'B':1, 'H': '0', '-':-9, 'NaN':-9})
	second_place = second_df.replace({'A':0,'B':1, 'H': '1','-':-9, 'NaN':-9})
	total = replaced.append(second_place)
	sorted = total.sort()
	sorted.to_csv('structure_input.csv', '\t', index=False, header=False)
	return(sorted)

if __name__ == '__main__':
    append()
