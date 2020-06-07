from new_coords import read_txt

info = read_txt('mercator_coords.txt')


while True:
    try:
        x, y, type, undertype, name, adress, *unused = input().split("; ")
        del unused
    except ValueError:
        print('Неверное кол-во аргументов')
    finally:
        break

print(adress)
