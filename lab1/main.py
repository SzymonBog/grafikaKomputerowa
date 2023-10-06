import numpy as np
from PIL import Image

# 1
obrazek = Image.open("inicjaly.bmp")
print("-------Informacje o obrazie")
print("tryb: ", obrazek.mode)
print("format: ", obrazek.format)
print("rozmiar: ", obrazek.size)

# 2
dane_obrazka = np.asarray(obrazek)

ob_d = Image.fromarray(dane_obrazka)
ob_d.show()

print("tryb:", ob_d.mode)
print("format:", ob_d.format)
print("rozmiar:", ob_d.size)

# 3
dane_obrazka = dane_obrazka * 1
print(dane_obrazka)

with open('inicjaly.txt', 'w') as f:
    for rows in dane_obrazka:
        for item in rows:
            f.write(str(item) + ' ')
        f.write('\n')
    f.close()

# 4
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:", dane_obrazka.itemsize)
print("pierwszy wyraz:", dane_obrazka[30][50])  # musi byc zastosowana inwersja(X,Y)->(Y,X)
print("drugi wyraz:", dane_obrazka[40][91])
print("trzeci wyraz:", dane_obrazka[0][99])
print("***************************************")  # wyniki sa ok

# 5
tb = np.loadtxt("inicjaly.txt", dtype=np.bool)

