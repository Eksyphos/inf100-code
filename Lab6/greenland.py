from pathlib import Path

def total_volume(path):
    content = Path(path).read_text(encoding='utf-8')
    data = content.splitlines()
    headers = data[0].split(',')
    area_col = headers.index('area_km2')
    thickness_col = headers.index('mean_thickness_m')
    volume = 0
    for line in data[1:]:
        liste = line.split(',')
        volume += int(liste[area_col])*(float(liste[thickness_col])/1000)
    return volume

def sea_level_rise(path):
    volume = total_volume(path)
    searise = round(volume/395000,1)
    return searise



# def test_total_volume():
#     print('Tester total_volume... ', end='')
#     a = round(total_volume('greenland.csv'))
#     print (a)
#     assert round(total_volume('greenland.csv')) == 2829200
#     print('OK')

# def test_sea_level_rise():
#     print('Tester sea_level_rise... ', end='')
#     assert sea_level_rise('greenland.csv') == 7.2
#     print('OK')

# # if __name__ == '__main__':
#     # test_total_volume()
#     # test_sea_level_rise()


