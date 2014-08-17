import pandas as pd
import get_snpcount
import parse_prop
import get_snpcount
import random


def add_sequences():
	'''STRUCTURE is more powerful if you have more individuals. So, if we have 
	   less than 10 individuals, add more. '''
	df = parse_prop.parse_prop()
	kage = get_snpcount.enough_info()
	kage = int(kage)
	if kage == 3:
		db =pd.read_csv('../data/3k_db.csv', sep='\t')
	elif kage == 6:
		db =pd.read_csv('../data/6k_db.csv', sep='\t')
	elif kage == 9:
		db =pd.read_csv('../data/9k_db.csv', sep='\t')
	elif kage == 19:
		db =pd.read_csv('../data/19k_db.csv', sep='\t')
	elif kage == 26:
		db =pd.read_csv('../data/26k_db.csv', sep='\t')
	else:
		db = pd.DataFrame()
	individs = len(df.index)
	needed = 10 - individs
	i = 0
	while i < needed:
		x = random.randint(1,(len(db.index)-1))
		row = db.iloc[x]
		df = df.append(row)
		i = i+1
	print df
	return(df)	
	
if __name__ == '__main__':
    add_sequences()
