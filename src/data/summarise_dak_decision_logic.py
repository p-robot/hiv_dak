"""
Summarise the decision logic variables within a HIV DAK decision logic Excel file

W. Probert, 2022
"""

import pandas as pd
import sys
from os.path import join

input_file = sys.argv[1] # "~/Downloads/HIV Digital Adaptation Kit Decision Logic-Draft 2022-02.xlsx"

# Read all sheets in the Excel file
df = pd.read_excel(input_file, sheet_name = None)

keys = list(df.keys())
n = len(keys)

pattern = "HIV\."

print(f"-----------------------------------")
print(f"This Excel file has {n} worksheets:\n")
for k in keys:
    print("\t | "+k)

# Count of which columns
count_cols = 0
count_vals = 0

print(f"\n\nWithin each worksheet, the following codes can be found:\n\n")
for k in keys:
    print(f"------------------------------------------------------")
    print(f"Processing columns of the worksheet titled ... ")
    print(k + "\n")
    print(f"------------------------------------------------------")

    for c in df[k].columns:
        print(f"Within the column named: {c}")
        if pattern in c:
            count_cols += 1
            print(count_cols)
            print(f" *** MATCH in the column name *** ")
        else: 
            print(f" --- No match in column name --- ")
        
        if any(df[k][c].astype(str).str.contains(pattern)):
            print(f" *** MATCH in the column values")
            vals = df[k][c][df[k][c].astype(str).str.contains(pattern)].values
            print(vals)
            count_vals += len(vals)
        else: 
            print(f" --- No match in column values --- ")
        print("\n")
    print("\n\n")

print(f"------------------------------------------------------")
print(f"Summary: ")
print(f"Number of columns with pattern: {count_cols}")
print(f"Number of column entries with pattern: {count_vals}")
print(f"------------------------------------------------------")
