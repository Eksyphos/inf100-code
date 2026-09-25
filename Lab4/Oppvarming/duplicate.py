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

def duplicate_2d(grid):
    for i in range(len(grid)):
        duplicate(grid[i])

def duplicated_2d(grid):
    newgrid = []
    for i in range(len(grid)):
        newgrid.append(duplicated(grid[i]))
    return newgrid



# def test_duplicate_2d():
# print('Testing duplicate_2d...', end=' ', flush=True)

# # Test 1
# arg = [
# [2, 3, 4],
# [4, 1, 0]
# ]
# return_val = duplicate_2d(arg)
# expected = [
# [4, 6, 8],
# [8, 2, 0]
# ]
# assert return_val is None
# assert expected == arg

# # Test 2
# arg = [[3, 2], [2, 1], [1, 0]]
# duplicate_2d(arg)
# duplicate_2d(arg)
# expected = [[12, 8], [8, 4], [4, 0]]
# assert expected == arg

# print('OK')
# test_duplicate_2d()
# def test_duplicated_2d():
# print('Testing duplicated_2d...', end=' ', flush=True)

# # Test 1
# arg = [
# [2, 3, 4],
# [4, 1, 0]
# ]
# return_val = duplicated_2d(arg)
# expected = [
# [4, 6, 8],
# [8, 2, 0]
# ]
# assert return_val == expected
# assert arg == [
# [2, 3, 4],
# [4, 1, 0]
# ]

# # Test 2
# arg = [[3, 2], [2, 1], [1, 0]]
# return_val = duplicated_2d(duplicated_2d(arg))
# expected = [[12, 8], [8, 4], [4, 0]]
# assert return_val == expected
# assert arg == [[3, 2], [2, 1], [1, 0]]

# print('OK')
# test_duplicated_2d()