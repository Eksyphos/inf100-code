

def longest_hot_period(temperatures, threshold):
    longest_start = -1
    longest_end = -1
    last_step = False
    longest_period = (0,0)
    if len([temp for temp in temperatures if temp >= threshold]) == 0:
        return (-1,-1)
    for i,temp in enumerate(temperatures):
        if temp>=threshold:
            if not last_step:
                longest_start = i
            last_step = True
        elif last_step:
            last_step = False
            longest_end = i
            x1,x2 = longest_period
            if abs(x1-x2)<abs(longest_start-longest_end):
                longest_period = (longest_start,longest_end)
            longest_start = i+1
        if i == len(temperatures)-1:
            longest_end = i+1
            x1,x2 = longest_period
            if abs(x1-x2)<abs(longest_start-longest_end):
                longest_period = (longest_start,longest_end)
    # print (longest_period)
    return longest_period



############## TESTER ##########
def test_longest_hot_period():
    print('Testing longest_hot_period... ', end='')
    temps = [25, 23, 19, 22, 24, 25, 21, 25, 26]

    threshold = 22
    expected_start, expected_end = 3, 6
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 23
    expected_start, expected_end = 0, 2
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 15
    expected_start, expected_end = 0, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 21
    expected_start, expected_end = 3, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 26
    expected_start, expected_end = 8, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 30
    expected_start, expected_end = -1, -1
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    print('OK')

if __name__ == '__main__':
    test_longest_hot_period()

