import pandas 
import read_file

def parse_prop():
	'''this file is in a weird, proprietary format. We import the file via \
	a homebrewed function called read_file, then do some munging to make it \
	into a structure-like file'''
	df = read_file.read_file()
	search = ['locusNames']
	for col in df.columns:
#Find the locus names. They're buried. Like treasure.
		if len(df[df[col].isin(search)]) > 0:
			locus_names = df[df[col].isin(search)]
			break
	search=['calls']
	for col in df.columns:
		if len(df[df[col].isin(search)]) > 0:
			calls = df[df[col].isin(search)]
	nuc_list = ['A','B','H']
	just_npns = calls[calls[:].isin(nuc_list)]
	just_snps = just_npns.dropna(axis=1)
	index = calls.iloc[:,0]
	new_index=[name.replace(" ","") for name in index]
	print new_index
	just_snps.insert(0, 'names',new_index)
	offset = len(just_snps.columns)
	col_names = locus_names.iloc[0,:offset]
	just_snps.columns = col_names
	just_snps.to_csv('structure_input.csv', '\t', index=False, header=True)
	return(just_snps)
##add function to populate structure file with more individuals to get more power.

if __name__ == '__main__':
    parse_prop()

