from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def figurePlot(images):
    fig = plt.figure(figsize=(32, 48))

    rows = int(len(images)/2)

    if len(images) % 2 == 1:
        rows += 1

    for i in range(rows):
        for j in range(2):
            if i*2+j < len(images):
                plt.subplot(rows, 2, i*2+j+1)
                plt.imshow(images[i*2+j])
                plt.axis('off')
    return fig

#1
obraz = Image.open("zeby.png")
print(obraz.mode)  # RGB
obraz = obraz.convert('L')

#2
#2.1 norm
def histogram_norm(obraz):
    hist = obraz.histogram()
    w, h = obraz.size
    N = w * h
    hist_norm = []
    for i in hist:
        hist_norm.append(i/N)
    return hist_norm


#2.2 cumul
def histogram_cumul(hist):
    hist_cumul = [hist[0]]
    for i in range(1, len(hist)):
        hist_cumul.append(hist_cumul[i-1] + hist[i])
    return hist_cumul


#2.3 equal
def histogram_equalization(obraz):
    hist_norm = histogram_norm(obraz)
    hist_cumul = histogram_cumul(hist_norm)
    obraz1 = obraz.point(lambda i: int(255 * hist_cumul[i]))
    return obraz1


#2.4
obraz21 = histogram_norm(obraz)
obraz22 = histogram_cumul(obraz21)
obraz23 = histogram_equalization(obraz)

obrazy = [obraz21, obraz22, obraz23]
fig1 = figurePlot(obrazy)
fig1.show()

#2.5
"""

"""

#3
obraz3 = ImageOps.equalize(obraz)

#3.1
obrazy = [obraz, obraz21, obraz22, obraz23, obraz3]
fig2 = figurePlot(obrazy)
fig2.show()

#3.2
"""

"""

#4
