import random
import json
from pathlib import Path



def main():
    content = Path('weights_en.json').read_text(encoding='utf-8')
    weights = json.loads(content)

    word_length = 12
    word = infer(word_length,weights)
    print(word)

def infer(word_length,weights):
    res = ''
    for _ in range (word_length):
        next_letter = get_token_ai(res,weights)
        res += next_letter
    return res

def get_token_ai(context,weights):
    relevant_context = context[-2:]
    vector = weights[relevant_context]
    letters = list(vector.keys())
    relative_prob = list(vector.values())
    random_letter = random.choices(letters, weights=relative_prob, k=1)[0]
    return random_letter




    return next_letter



if __name__ == '__main__':
    main()