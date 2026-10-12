from pathlib import Path

content = Path('nsf2025.txt').read_text(encoding='utf-8')

counts = {
    'a':0,
    'b':0,
    'c':0,
}


for letter in content:
    if letter in counts:
        counts[letter] = counts[letter] +1
    else:
        counts[letter]=1


for key in counts:
    print(f'{key}:{counts[key]}')