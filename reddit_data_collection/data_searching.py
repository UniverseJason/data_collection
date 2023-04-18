import pandas as pd
import csv
from tqdm import tqdm

infile = "./data_archive/cleaned_reddit_data.csv"
line_number = 44998748

reader = pd.read_csv(infile, chunksize=10000, iterator=True)

# print the number of the distinguished columns if it is not empty
counter = 0
progress_bar = tqdm(total=line_number)
for chunk in tqdm(reader):
    for index, row in chunk.iterrows():
        if row['distinguished'] != '':
            print(index)
            print(row['distinguished'])
            counter += 1
    progress_bar.update(10000)
