from pathlib import Path
import json
def main():
    train('words_en.txt','weights_en.json')
    train('words_no.txt','weights_no.json')

def train(training_Data_filename,weights_filename):
    content = Path(training_Data_filename).read_text(encoding='utf-8')
    lines = content.splitlines()

    weights = {}
    for word in lines:
        extend_weights(weights,word)



    weights_string = json.dumps(weights)
    Path(weights_filename).write_text(weights_string,encoding='utf-8')


def extend_weights(weights,word):
    ''

    for i in range(len(word)):
        left = word[:i]
        candidate_token = word[i]
        
        for context_size in range(1,3):

            relevant_context = left[-context_size:]
            if relevant_context not in weights:
                weights[relevant_context] = {}

            vector = weights[relevant_context]
            if candidate_token not in vector:
                vector[candidate_token] = 0
            vector[candidate_token] += 1



if __name__=='__main__':
    main()