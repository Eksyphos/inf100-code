import os
import csv
from pathlib import Path

def combine_csv_in_dir(dirpath, result_path):
    filepath_list = Path(dirpath).glob('*.csv')
    templist = []
    for filepath in filepath_list:
        file = Path(filepath).open()
        filtered = csv.reader(file)
        for temp in filtered:
            templist.append(temp)
    print(templist)

if __name__=="__main__":
    dirpath = os.path.join(os.path.dirname(__file__), "samples")
    combine_csv_in_dir(dirpath, "combined_table.csv")