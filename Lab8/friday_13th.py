from datetime import datetime,date
def first_friday_13th_after(date1):
    year = date1.year
    while True:
        for month in range(1,13):
            if is_it_friday13th(date(year,month,13)):
                if date1<datetime(year,month,13):
                    return datetime(year,month,13)
        year +=1
        if year>3000:
            return TimeoutError

def is_it_friday13th(date):
    return date.weekday() == 4 and date.day==13






############### TESTER ################
def test_first_friday_13th_after():
    print('Tester first_friday_13th_after... ', end='')
    # Test 1
    result = first_friday_13th_after(datetime(2022, 10, 24))
    assert (2023, 1, 13) == (result.year, result.month, result.day)
    # Test 2
    result = first_friday_13th_after(datetime(2023, 1, 13))
    assert (2023, 10, 13) == (result.year, result.month, result.day)
    # Test 3
    result = first_friday_13th_after(datetime(1950, 1, 1))
    assert (1950, 1, 13) == (result.year, result.month, result.day)
    print('OK')

if __name__=='__main__':
    test_first_friday_13th_after()