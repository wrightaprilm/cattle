import pandas as pd

def get_sites(df):
	sites = len(df.columns)
	sites = sites - 2 
	print sites
	indices = len(df.index)
	return([sites,indices])

if __name__ == '__main__':
    get_sites(df)
