<<<<<<< Updated upstream
from new_coords import read_txt

info = read_txt('mercator_coords.txt')
=======
while True:
    try:
        x, y, type, undertype, name, adress = input().split(";")
    except ValueError:
        print('Неверное кол-во аргументов')
    finally:
        if adress[1] == ';':
            adress = adress[0]
        break

print(x, y, type, undertype, name, adress)
>>>>>>> Stashed changes
