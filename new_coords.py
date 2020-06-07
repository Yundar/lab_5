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


print(info('ukraine_poi.csv'))
