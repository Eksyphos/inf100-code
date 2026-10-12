from pathlib import Path

lines = Path('csv.csv').read_text(encoding='utf-8')
headers = lines[0].split(',')
data_lines=lines[1:].split(',')
number_of_cols = len(headers)

table_dict = []
for line in data_lines:
    row_dict = {}

    cells = line.split(',')
    for i in range(number_of_cols):
        row_dict.append(f'') 


print (content)