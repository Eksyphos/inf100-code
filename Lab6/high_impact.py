from pathlib import Path


def get_impact(line):
    impact = line.split(';')
    try:
        return float(impact[2])
    except:
        return None

def filter_earthquakes(earthquake_csv_string, threshold):
    content = earthquake_csv_string.splitlines()
    headers = content[0]
    newcontent = []
    for line in content[1:]:
        if get_impact(line)!= None and get_impact(line)>threshold:
            newcontent.append(line)
    newcontent.insert(0,headers)
    returnstring = ''
    for line in newcontent:
        returnstring += f'{line}\n'
    return returnstring
        
def filter_earthquakes_file(source_filename, target_filename, threshold):
    content = Path(source_filename).read_text(encoding='utf-8')
    data = filter_earthquakes(content,threshold)
    Path(target_filename).write_text(data,encoding='utf-8')




################### TESTING ##################

def test_get_impact():
    print('Tester get_impact... ', end='')
    assert 1.43 == get_impact('nc72666881;California;1.43;2016-07-27 00:19:43')
    assert 4.9 == get_impact('us20006i0y;Burma;4.9;2016-07-27 00:20:28')
    assert None is get_impact('us20006i0y;Burma;not_a_num;2016-07-27 00:20:28')
    print('OK')

def test_filter_earthquakes():
    print('Tester filter_earthquakes... ', end='')
    input_arg = '''\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
nc72666892;California;not_a_number;2016-08-23 03:21:18
'''
    # Test 1
    expected_value = '''\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
'''
    actual_value = filter_earthquakes(input_arg, 1.1)
    assert expected_value.strip() == actual_value.strip()

    # Test 2
    expected_value = '''\
id;location;impact;time
us20006i0y;Burma;4.9;2016-07-27 00:20:28
''' 
    actual_value = filter_earthquakes(input_arg, 3.0)
    assert expected_value.strip() == actual_value.strip()

    # Test 3
    expected_value = 'id;location;impact;time\n'
    actual_value = filter_earthquakes(input_arg, 5.0)
    assert expected_value.strip() == actual_value.strip()
    print('OK')


if __name__ == '__main__':
    test_get_impact()
    test_filter_earthquakes()
