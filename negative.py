from matplotlib import pyplot as plot
import numpy as np
import cv2
import sys


img = cv2.imread('apple.jpeg')
cv2.imshow('img',img)
inverted = np.abs(img - 255)

def inverte(imagem, name):
    imagem = (255-imagem)
    imagem = cv2.bitwise_not(imagem)


def inverte2(imagem, name):
    for x in np.nditer(imagem, op_flags=['readwrite']):
        pass
    imagem = cv2.bitwise_not(imagem)

if __name__== '_main_':
    (imgB, imgG, imgR) = cv.split(img)
    imageB = negativ(imgB)
    imageG = negativ(imgG)
    imageR = negativ(imgR)
    image = cv.merge((imageR, imageG, imageB))


cv2.waitKey(0)
plot.figure(2)
plot.imshow(img)
plot.title('Negatif Goruntu', fontweight="bold")

plot.show()
