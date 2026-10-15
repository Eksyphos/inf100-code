from pathlib import Path

def get_stringsum(s):
    sumtotal = 0
    wordlist = s.split(' ')
    for word in wordlist:
        try:
            sumtotal += int(word)
        except:
            continue
    return sumtotal

def get_line_with_highest_stringsum(s):
    wordlines = s.splitlines()
    highestvalue = 0
    highestline = ''
    highestindex = 0

    for index,line in enumerate(wordlines):
        linesum = get_stringsum(line)
        if linesum>highestvalue:
            highestvalue = linesum
            highestline = line
            highestindex = index+1
    bestline = (highestindex,highestvalue,highestline)
    return bestline

def main():
    userinput = input('Filnavn: ')
    content = Path(userinput).read_text(encoding='utf-8')
    data = get_line_with_highest_stringsum(content)
    index,val,line = data
    print(f'Høyeste strengsum er {val}, funnet først på linje {index}: «{line}»')

if __name__ == '__main__':
    main()