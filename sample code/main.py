import cv2
import numpy as np
from extract import extract
from color import color
from number import number

COL = 0       # R=0, G=1, P=2
NUM = 1       # 1=1, 2=2, 3=3
SHADE = 2     # E=0, S=1, F=2
SHAPE = 3     # O=0, D=1, S=2
NCARDS = 9

res = np.empty([9, 4], dtype=np.uint8)

card = extract('set.jpg', NCARDS)

for i in range(NCARDS):
    res[i, COL] = color(card[i])
    res[i, NUM] = number(card[i])

print(res)
