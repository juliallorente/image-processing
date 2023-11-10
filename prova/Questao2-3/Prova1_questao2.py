import cv2
import numpy as np
import matplotlib.pyplot as plt

# lendo a imagem e normalizando os valores dos pixels
M = cv2.imread('Lighthouse_bayerBG8.png', cv2.IMREAD_GRAYSCALE)
M = np.pad(M, [(1, 1), (1, 1)], mode='constant')  # adiciona uma moldura de zeros
M = M / 255

height = len(M)
width = len(M[0])
rgb = np.zeros((height-2, width-2, 3))

# aplicação filtro de bayer
for i in range(1, height-1):
    for j in range(1, width-1):
        if(i % 2 == 1 and j % 2 == 1): # azul
            r = round(255 * (M[i-1,j-1] + M[i+1,j+1] + M[i-1,j+1] + M[i+1,j-1]) / 4)
            g = round(255 * (M[i,j-1] + M[i,j+1] + M[i-1,j] + M[i+1,j]) / 4)
            b = 255 * M[i,j]
        elif(i % 2 == 0 and j % 2 == 0): # vermelho
            r = 255 * M[i,j]
            g = round(255 * (M[i,j-1] + M[i,j+1] + M[i-1,j] + M[i+1,j]) / 4)
            b = round(255 * (M[i-1,j-1] + M[i+1,j+1] + M[i-1,j+1] + M[i+1,j-1]) / 4)
        elif(i % 2 == 1 and j % 2 == 0): # verde 1
            r = round(255 * (M[i-1,j] + M[i+1,j]) / 2)
            g = 255 * M[i,j]
            b = round(255 * (M[i,j-1] + M[i,j+1]) / 2)
        elif(i % 2 == 0 and j % 2 == 1): # verde 2
            r = round(255 * (M[i,j-1] + M[i,j+1]) / 2)
            g = 255 * M[i,j]
            b = round(255 * (M[i-1,j] + M[i+1,j]) / 2)
        rgb[i-1,j-1,0] = r
        rgb[i-1,j-1,1] = g
        rgb[i-1,j-1,2] = b

# cria a imagem
img1 = np.array(rgb, dtype=np.uint8)

# salva a imagem
cv2.imwrite('output_imagem.jpg', cv2.cvtColor(img1, cv2.COLOR_RGB2BGR))

# printa a imagem
plt.imshow(img1)
plt.show()
