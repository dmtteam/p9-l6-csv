import sys
import csv
import os
# import pickle
# import json

zawartosc_pliku = []
ile_wierszy = 0


def istnieje(plik):
    if os.path.exists(plik):
        # print("OK")
        return True
    else:
        print('NieMo pliku ale zobacz co jest w tym katalogu:')
        katalog = list(os.listdir())
        print(katalog)
        return False


if not istnieje(sys.argv[1]):
    sys.exit()

# open file
with open(sys.argv[1], "r", newline="") as f:
    reader = csv.reader(f)
    for line in reader:
        ile_wierszy = ile_wierszy + 1
        zawartosc_pliku.append(line)

# change file
for zmiana in sys.argv[3:]:
    parametry = zmiana.split(",")
    wiersz = int(parametry[0]) - 1

    # rows in range ?
    if (wiersz + 1) > ile_wierszy or (wiersz - 1) == 0 or wiersz < 0:
        print(f'Nr wiersza po za zakresem. Min to 1, max to:', ile_wierszy)
        sys.exit()

    # columns in range?
    kolumna = int(parametry[1]) - 1
    max_kolumna = len(line)
    if int(parametry[1]) > max_kolumna or int(parametry[1]) <= 0:
        print(f'Nr kolumny po za zakresem.Min to 1, max to:', max_kolumna)
        sys.exit()

    wartosc = parametry[2]
    zawartosc_pliku[wiersz][kolumna] = wartosc

# save file
with open(sys.argv[2], "w", newline="") as f:
    writer = csv.writer(f)
    for line in zawartosc_pliku:
        writer.writerow(line)
        print(line)
