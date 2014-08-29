import pandas 
import read_file

def parse_prop(df):
	'''this file is in a weird, proprietary format. We import the file via \
	a homebrewed function called read_file, then do some munging to make it \
	into a structure-like file'''
	search = ['locusNames']
	other_search = [' GTS LocusId']
	third_search = ['locusName']
	fourth_search = ['LocusName']
	fifth_search = ['LocusNames']
	for col in df.columns:
#Find the locus names. They're buried. Like treasure.
		if len(df[df[col].isin(search)]) > 0:
			locus_names = df[df[col].isin(search)]
			print 'Locus names located'
			break
		elif len(df[df[col].isin(other_search)]) > 0:
			locus_names = df[df[col].isin(other_search)]
			print locus_names
			break
		elif len(df[df[col].isin(third_search)]) > 0:
			locus_names = df[df[col].isin(third_search)]
			print 'Locus names located'
			break
		elif len(df[df[col].isin(fourth_search)]) > 0:
			locus_names = df[df[col].isin(fourth_search)]
			print 'Locus names located'
			break
		elif len(df[df[col].isin(fifth_search)]) > 0:
			locus_names = df[df[col].isin(fifth_search)]
			print 'Locus names located'
			break
		else:
			print 'Searching for locus names'

	search=['calls']
	for col in df.columns:
		if len(df[df[col].isin(search)]) > 0:
			calls = df[df[col].isin(search)]
			print 'Data Located'
			break
		else:
			print 'Looking for data'
	nuc_list = ['A','B','H']
	just_npns = calls[calls[:].isin(nuc_list)]
	just_snps = just_npns.dropna(axis=1)
	index = calls.iloc[:,0]
	new_index=[name.replace(' ',"") for name in index]
	just_snps.index = new_index
	offset = len(just_snps.columns)
	col_names = locus_names.iloc[0,:offset]
	just_snps.columns = col_names
	return(just_snps)

if __name__ == '__main__':
    parse_prop(df)

