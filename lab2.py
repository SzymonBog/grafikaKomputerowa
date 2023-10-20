import numpy as np
from PIL import Image


# zadanie 1
def rysuj_ramke_w_obrazie(obraz, grub):
    inicjaly = Image.open(obraz)
    obraz_wstawiany = np.asarray(inicjaly) * 1
    h, w = obraz_wstawiany.shape
    # print(f"{h}x{w}")
    # obraz_wstawiany[grub:h - grub, grub:w - grub] = 0
    for i in range(h):
        for j in range(grub):
            obraz_wstawiany[i][j] = 0
            obraz_wstawiany[i][w - 1 - j] = 0
    for i in range(w):
        for j in range(grub):
            obraz_wstawiany[j][i] = 0
            obraz_wstawiany[h - 1 - j][i] = 0
    print(obraz_wstawiany)

    obraz_wstawiany = np.array(obraz_wstawiany, dtype=bool)

    ob = Image.fromarray(obraz_wstawiany)
    ob.show()
    return ob


# zadanie 2
i1 = rysuj_ramke_w_obrazie("inicjaly.bmp", 10)
i2 = rysuj_ramke_w_obrazie("inicjaly.bmp", 5)
i1.save("ramka10.bmp")
i2.save("ramka5.bmp")


# zadanie 3 podpunkt 1.1
def rysuj_ramke(w, h, grub, t, powtorzenia):
    obraz = np.zeros(t, dtype=np.uint8)
    for i in range(powtorzenia):
        if i % 2 == 0:
            obraz[grub * i:h - grub * i, grub * i:w - grub * i] = 0
        else:
            obraz[grub * i:h - grub * i, grub * i:w - grub * i] = 1
    obraz = obraz.astype(np.bool_)
    return obraz


def zad31(w, h, grub):
    t = (h, w)
    ob = np.zeros((h, w), dtype=np.uint8)
    num = (h // 2) // grub
    print(num)

    ob = rysuj_ramke(w, h, grub, t, num)
    ob=Image.fromarray(ob)
    ob.show()
    return ob

# zadanie 3 podpunkt 1.1 wywołanie funkcji
zad31(400, 300, 4)

# zadanie 3 podpunkt 1.2
def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    ob = np.ones(t, dtype=np.uint8)
    count = int(w/grub)
    print(count)
    for k in range(count):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                ob[j, i] = k % 2

    ob = ob * 255
    ob = Image.fromarray(ob)
    ob.show()
    return ob


def zad32(w, h, grub):
    ob = rysuj_pasy_pionowe(w, h, grub)
    return ob

# zadanie 3 podpunkt 1.2 wywołanie funkcji
zad32(400, 300, 37)

# zadanie 3 podpunkt 1.3
def styk(w, h, m, n):
    ob = np.zeros((h, w), dtype=np.uint8)  # [0-59][0-119]
    if (0 > m or m > w-1) and (0 > n or n > h-1):
        print(f"index {m} is out of bounds for axis 0 with size 120 and\nindex {n} is out of bounds for axis 0 with size 60")
    elif 0 > m or m > w-1:
        print(f"index {m} is out of bounds for axis 0 with size 120")
    elif 0 > n or n > h-1:
        print(f"index {n} is out of bounds for axis 0 with size 60")
    else:
        print("ok")
        ob[n:h, 0:m] = 1
        ob[0:n, m:w] = 1
        print(ob)
    ob = ob.astype(np.bool_)
    ob = Image.fromarray(ob)
    ob.show()
    return ob


def zad33(w, h, m, n):
    ob = styk(w, h, m, n)
    return ob

# zadanie 3 podpunkt 1.3 wywołanie funkcji
zad33(120, 60, 80, 10)

# zadanie 3 podpunkt 1.4
def checkers(w, h, grub):  # szachownica o dowolnej grubosci pol
    ob = np.zeros((h, w), dtype=np.uint8)
    nr = 0
    color = 1
    startingColor = color
    for i in range(h):
        for j in range(w):
            if j % grub == 0:
                if color == 1:
                    color = 0
                else:
                    color = 1
            ob[i, j] = color

        if (nr+1) % grub == 0:
            if startingColor == 0:
                color = 1
            else:
                color = 0
            startingColor = color
        else:
            color = startingColor
        nr += 1
    print(ob)

    ob = ob.astype(np.bool_)
    ob = Image.fromarray(ob)
    ob.show()
    return ob


def zad34(w, h, grub):
    ob = checkers(w, h, grub)
    return ob

# zadanie 3 podpunkt 1.4 wywołanie funkcji
zad34(120, 60, 5)


# zadanie 4
def zad4():
    w, h, grub, m, n = 480, 320, 10, 100, 50
    i1 = zad31(w, h, grub)
    i2 = zad32(w, h, grub)
    i3 = zad33(w, h, m, n)
    i4 = zad34(w, h, grub)
    i1.save("zad41.bmp")
    i2.save("zad42.bmp")
    i3.save("zad43.bmp")
    i4.save("zad44.bmp")

# zadanie 4 wywołanie funkcji
zad4()

# zadanie 5
def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_obraz = np.asarray(obraz_bazowy)*1
    h0, w0 = tab_obraz.shape
    t = (h0, w0)
    tab_obraz_wst = np.asarray(obraz_wstawiany) * 1
    h1, w1 = tab_obraz_wst.shape
    n_k = min(h1, n+h0)
    m_k = min(w1, m+w0)
    n_p = max(0, n)
    m_p = max(0, m)
    print(n_k, m_k)
    print(n_p, m_p)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_obraz_wst[i][j] = tab_obraz[i-n][j-m]
    tab = tab_obraz_wst.astype(bool)
    return Image.fromarray(tab)


def zad5(obraz_bazowy, obraz_wstawiany, m, n):
    x = wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n)
    x.show()
    return x

# zadanie 5 wywołanie funkcji
inicjaly = Image.open("inicjaly.bmp")
obraz1 = Image.open("zad42.bmp")

z51 = zad5(inicjaly, obraz1, 300, 90)
z52 = zad5(inicjaly, obraz1, 10, 290)

z51.save("wstaw1.bmp")
z52.save("wstaw2.bmp")
