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


write_new_cords(info('ukraine_poi.csv'))
print(read_txt('mercator_coords.txt'))
