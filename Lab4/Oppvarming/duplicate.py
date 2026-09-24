def duplicate(numbers):
    c = 0
    for number in numbers:
        numbers[c] = number*2
        c +=1

def duplicated(numbers):
    dobbelt = []
    for num in numbers:
        dobbelt.append(num*2)
    return dobbelt
