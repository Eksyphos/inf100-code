def compress(raw_binary):
    count = 0
    truecount = 0
    lastdigit = 0
    compressed=[]
    for i in raw_binary:
        truecount+=1
        i = int(i)
        if i == lastdigit:
            count+=1
        else:
            compressed.append(count)
            lastdigit = i
            count=1
    if truecount==len(raw_binary):
        compressed.append(count)
    return compressed

def decompress(compressed_binary):
    string=""
    for i in range(len(compressed_binary)):
        if i%2==0:
            string+="0"*compressed_binary[i]
        else:
            string+="1"*compressed_binary[i]
    return string

# def test_compress():
#     print('Tester compress... ', end='')
#     assert([2, 3, 4, 4] == compress('0011100001111'))
#     assert([0, 2, 1, 8, 1] == compress('110111111110'))
#     assert([4] == compress('0000'))
#     print('OK')

# def test_decompress():
#     print('Tester decompress... ', end='')
#     assert('0011100001111' == decompress([2, 3, 4, 4]))
#     assert('110111111110' == decompress([0, 2, 1, 8, 1]))
#     assert('0000' == decompress([4]))
#     print('OK')

# test_compress()
# test_decompress()