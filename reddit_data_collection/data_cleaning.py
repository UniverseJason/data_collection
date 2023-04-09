import pandas as pd
import csv
from tqdm import tqdm

input_file = "new_reddit_data.csv"
output_file = "filtered_reddit_data.csv"
total_lines = 45000001
chunksize = 1000

df = pd.read_csv(input_file, chunksize=chunksize)
progress_bar = tqdm(total=total_lines)

with open(output_file, 'w', newline='', encoding='utf-8') as filtered_file:
    for i, chunk in enumerate(df):
        # Remove rows with empty values in the first column
        chunk = chunk.dropna(subset=[chunk.columns[0]])
        
        if i == 0:  # Write the header and the first chunk
            chunk.to_csv(filtered_file, index=False, quoting=csv.QUOTE_NONNUMERIC)
        else:  # Append the subsequent chunks without the header
            chunk.to_csv(filtered_file, index=False, header=False, quoting=csv.QUOTE_NONNUMERIC)
        
        progress_bar.update(chunksize)

progress_bar.close()
print(f"Filtered data written to {output_file}")
