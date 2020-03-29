import csv
import pandas as pd


my_csv = pd.read_csv('SARSCoV_meta.tsv', usecols=['strain.1','virus','accession','date','region', 'country'], sep='\t')
my_csv = my_csv.rename(columns={"accession": "assession", 'strain.1':'strain'})
my_csv = my_csv[['strain','virus','assession','date','region', 'country']]
print(my_csv)
my_csv.to_csv('./SARSCoV_meta.tsv', sep='\t', index=False)
