import csv
from pathlib import Path
def count_facilities_by_species(path):
    content = Path(path).read_text()
    data = content.splitlines()

    fishdict = {}
    for line in data[2:]:
        line = line.split(';')
        if line[12] in fishdict:
            fishdict[line[12]] +=1
        else:
            fishdict.update({line[12]:1})
    for key in sorted(fishdict):
        print(f'{key}: {fishdict[key]}')






if __name__ == '__main__':
    count_facilities_by_species('Akvakulturregisteret.csv')