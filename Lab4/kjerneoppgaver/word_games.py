def can_be_made_of_letters(word,letters):
    letterlist = list(letters)
    for letter in word:
        if letter in letterlist:
            letterlist.remove(letter)
        elif "*" in letterlist:
            letterlist.remove("*")
        else:
            return False
    return True

def possible_words(wordlist, letters):
    Pwords = []
    for word in wordlist:
        if can_be_made_of_letters(word,letters):
            Pwords.append(word)
    return Pwords
