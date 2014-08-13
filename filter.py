import pandas as pd
import sys
import csv
import StringIO
#lines=list(csv.reader(open(sys.argv[1])))
lines=list(csv.reader(open('CTL 3K 06jul2011_LocusXDNA.csv')))
df =pd.DataFrame(lines)


search = ['locusNames']
for col in df.columns:
    if len(df[df[col].isin(search)]) > 0:
        locus_names = df[df[col].isin(search)]
        break

df.columns = df.iloc[1]

search=['calls']
for col in df.columns:
    if len(df[df[col].isin(search)]) > 0:
        calls = df[df[col].isin(search)]
nuc_list = ['A','B','H']
just_npns = snps[snps[:].isin(nuc_list)]
just_snps = just_npns.dropna(axis=1)

index = snps.iloc[:,0]
just_snps.insert(0, 'names',index)

offset = len(just_snps.columns)
col_names = locus_names.iloc[0,:offset]
just_snps.columns = col_names
second_df = just_snps
replaced = just_snps.replace({'A':0,'B':1, 'H': '0'})
second_place = second_df.replace({'A':0,'B':1, 'H': '1'})
total = replaced.append(second_place)
sorted = total.sort()


sorted.to_csv('snps.csv','\t', index=False)

