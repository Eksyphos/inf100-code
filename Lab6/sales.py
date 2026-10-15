from pathlib import Path

def total_income(path):
    content = Path(path).read_text(encoding='utf-8')
    lines = content.splitlines()
    headers = lines[0].split(',')
    prod_col = headers.index('production_cost')
    price_col = headers.index('price')
    sold_col = headers.index('sold')
    earnings = 0
    for line in lines[1:]:
        line = line.split(',')
        earnings += (int(line[price_col])-int(line[prod_col]))*int(line[sold_col])
    return earnings

