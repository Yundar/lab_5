import math
import codecs


def info(path):
    file = codecs.open(path, 'r', 'utf_8_sig')
    file_content = file.readlines()
    array = []
    l = len(file_content)
    for i in range(l):
        file_content[i] = file_content[i][0:-1]
        file_content[i] = list(file_content[i].split(';'))
        if file_content[i][0] != '':
            file_content[i][0], file_content[i][1] = float(file_content[i][0].replace(',', '.')), float(
                file_content[i][1].replace(',', '.'))
            array.append(file_content[i])
    return array


def lat_lon_to_mer(array):
    a = 6378137.0
    b = 6356752.3142
    for i in range(len(array)):
        lat = array[i][0]
        long = array[i][1]
        if lat > 89.5:
            lat = 89.5
        if lat < -89.5:
            lat = -89.5
        r_lat = math.radians(lat)
        r_long = math.radians(long)
        f = (a - b) / a
        e = math.sqrt(2 * f - f ** 2)
        x = a * r_long
        y = a * math.log(
            math.tan(math.pi / 4 + r_lat / 2) * ((1 - e * math.sin(r_lat)) / (1 + e * math.sin(r_lat))) ** (e / 2))
        array[i][1], array[i][0] = x, y
    return array


def write_new_cords(array):
    output = codecs.open('mercator_coords.txt', 'w', 'utf_8_sig')
    for i in array:
        for j in i:
            output.write(str(j) + ';')
        output.write('\n')


def read_txt(path):
    file = codecs.open(path, 'r', 'utf_8_sig')
    file_content = file.readlines()
    array = []
    for i in range(len(file_content)):
        file_content[i] = file_content[i][0:-1]
        file_content[i] = list(file_content[i].split(';'))
        if file_content[i][0] != '':
            file_content[i][0], file_content[i][1] = float(file_content[i][0]), float(file_content[i][1])
        array.append(file_content[i])
    return array


write_new_cords(lat_lon_to_mer(info('ukraine_poi.csv')))
