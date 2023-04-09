import pandas as pd
import csv
from tqdm import tqdm

total_lines = 53851543
new_size = 45000000
chunksize = 10000
num_chunks = (new_size + chunksize - 1) // chunksize
reader = pd.read_csv('RC_2015-01.csv', chunksize=chunksize, on_bad_lines='skip')
row_count = 0

with open('new_reddit_data.csv', 'w', newline='') as new_file:
    for i, chunk in enumerate(tqdm(reader, total=num_chunks)):
        if row_count >= new_size:
            break
        remaining_rows = new_size - row_count
        chunk = chunk.head(remaining_rows)
        row_count += len(chunk)

        if i == 0:  # Write the header and the first chunk
            chunk.to_csv(new_file, index=False, quoting=csv.QUOTE_NONNUMERIC)
        else:  # Append the subsequent chunks without the header
            chunk.to_csv(new_file, index=False, header=False, quoting=csv.QUOTE_NONNUMERIC)

print(f'First {row_count} rows written to new_RC_2015-01.csv')
