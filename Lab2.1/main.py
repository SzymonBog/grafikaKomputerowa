import numpy as np
from PIL import Image


# 1
def rysuj_ramke_w_obrazie(obraz, grub):
    inicjaly = Image.open(obraz)
    obraz_wstawiany = np.asarray(inicjaly)*1
    h, w = obraz_wstawiany.shape
    # print(f"{h}x{w}")
    # obraz_wstawiany[grub:h - grub, grub:w - grub] = 0
    for i in range(h):
        for j in range(grub):
            obraz_wstawiany[i][j] = 0
            obraz_wstawiany[i][w-1-j] = 0
    for i in range(w):
        for j in range(grub):
            obraz_wstawiany[j][i] = 0
            obraz_wstawiany[h-1-j][i] = 0
    print(obraz_wstawiany)

    obraz_wstawiany = np.array(obraz_wstawiany, dtype=bool)

    ob = Image.fromarray(obraz_wstawiany)
    ob.show()
    return ob


# 2
i1 = rysuj_ramke_w_obrazie("sb.bmp", 10)
i2 = rysuj_ramke_w_obrazie("sb.bmp", 5)
i1.save("ramka10.bmp")
i2.save("ramka5.bmp")

# 3
def rysuj_ramke(w, h, grub):
    print()
    
def zad31(w, h, grub):
    ob = np.zeros((h, w), dtype=np.uint8)
    num = h//grub
    print(num)
    for i in range(num):
        print("dokoncz")
zad31(100, 100, 16)
