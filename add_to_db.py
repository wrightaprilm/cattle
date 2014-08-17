import pandas as pd
import get_snpcount
import parse_prop

def add_to_base():
	'''Add new next-gen data to database of appropriate SNP size. Will use 
	Pandas join to do this. '''
	kage = get_snpcount.enough_info()
	kage = int(kage)
	if kage == 3:
		db =pd.read_csv('../data/3k_db.csv', sep='\t')
		fname = '../data/3k_db.csv'
	elif kage == 6:
		db =pd.read_csv('../data/6k_db.csv', sep='\t')
		fname = '../data/6k_db.csv'
	elif kage == 9:
		db =pd.read_csv('../data/9k_db.csv', sep='\t')
		fname = '../data/9k_db.csv'
	elif kage == 19:
		db =pd.read_csv('../data/19k_db.csv', sep='\t')
		fname = '../data/19k_db.csv'
	elif kage == 26:
		db =pd.read_csv('../data/26k_db.csv', sep='\t')
		fname = '../data/26k_db.csv'
	else:
		db = pd.DataFrame()
	new_data = parse_prop.parse_prop()
	total_df = db.append(new_data)
	new_data.to_csv(fname,'\t', index=False, header=False, mode='a')
	return(total_df)

if __name__ == '__main__':
    add_to_base()


