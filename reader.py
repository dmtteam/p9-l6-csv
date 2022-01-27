import sys
import csv
import os
import pickle
import json

zawartosc_pliku = []        # co w pliku
zmiany = []                 # lista wszystkich zmian z argv 3 do n

def istnieje(plik):
    if os.path.exists(plik):
        # print("ok")
        return True
    else:
        print('NieMo pliku ale zobacz co jest w tym katalogu:')
        katalog = list(os.listdir())
        # for jakie in katalog:
        print(katalog)
        return False

istnieje(sys.argv[1])

with open(sys.argv[1], "r",  newline="") as f:
    reader = csv.reader(f)
    for line in reader:
        zawartosc_pliku.append(line)
        print(" ".join(line))


# .strip()
zmiana = (sys.argv[3:])
zmiany.append(zmiana)
print(zmiany)

with open(sys.argv[2], "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(zawartosc_pliku)
    writer.writerow(zmiany)


# delimiter =' ',quotechar =','
