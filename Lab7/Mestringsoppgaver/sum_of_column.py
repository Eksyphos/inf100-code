from pathlib import Path
from csv import reader
def sum_of_column(path,col):
    content = Path(path).read_text(encoding='utf-8')
    lines = content.splitlines()
    the_sum = 0.0
    for line in reader(lines):
        try:
            the_sum += float(line[col])
        except:
            continue
    print(the_sum)
    return the_sum