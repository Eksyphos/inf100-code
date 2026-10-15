from pathlib import Path

def best_alignment(genome,sequence):
    best_match = 0
    matchlevel = 0
    SeqLength = len(sequence)
    for i in range(len(genome)):
        if SeqLength+i >len(genome):
            break
        genome_part = genome[i:SeqLength+i]
        check_value = check_match(genome_part,sequence)
        if check_value>matchlevel:
            matchlevel = check_value
            best_match = i
    return best_match  

def check_match(genomepart,sequence):
    matches = 0
    for i in range(len(genomepart)):
        try:
            if genomepart[i]==sequence[i]:
                matches +=1
        except:
            continue
    return matches

def best_alignment_to_file(path,sequence):
    content = Path(path).read_text(encoding='utf-8')
    matchindex=best_alignment(content,sequence)
    return matchindex



def test_best_alignment():
    print('Testing best_alignment...', end='')
    genome = 'AAACACCCCCGGGGGTGTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    sequence = 'ACACCCCCGGGGATGT'
    assert 2 == best_alignment(genome, sequence)

    genome = 'AAAAAAAAAAAAAAAAACACCCCCGGGGGTGTTTTTTTTTTTTTT'
    sequence =                     'CCGGGGATGT'
    assert 22 == best_alignment(genome, sequence)

    genome = 'TTTAAG'
    sequence = 'AAGT'
    assert 2 == best_alignment(genome, sequence)
    print(' OK')

def test_best_alignment_to_file():
    print('Testing best_alignment_to_file...', end='')
    path = 'human_genome_excerpt.txt'
    assert 30864 == best_alignment_to_file(path, 'AAACAAAGAA')
    assert 2097 == best_alignment_to_file(path, 'GAGTGGGATGAGCCATTGTTCATCT')
    assert 0 == best_alignment_to_file(path, 'TAACCC' * 18)
    assert 49913 == best_alignment_to_file(path, 'CATTTCAGTAGTAATAGGAATCTCCAC')
    print(' OK')

test_best_alignment()
test_best_alignment_to_file()

