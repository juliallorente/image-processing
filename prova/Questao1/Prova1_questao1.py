import cv2
import numpy as np

# imagens de teste: red.png, blue.png, green.png, black.png and white.png
img = cv2.imread("imagens_testes/blue.png")
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# calcula a média dos valores dos pixels para cada canal de cor
mediaR = np.average(r)
mediaG = np.average(g)
mediaB = np.average(b)

# normaliza as médias para estarem entre 0 e 1
R = round(mediaR/255)
G = round(mediaG/255)
B = round(mediaB/255)

# compara os valores normalizados para determinar a cor da imagem
if   (R==1 and G==0 and B==0): print("Red")
elif (R==0 and G==1 and B==0): print("Green")
elif (R==0 and G==0 and B==1): print("Blue")
elif (R==0 and G==0 and B==0): print("Black")
elif (R==1 and G==1 and B==1): print("White")
else: print("undefined")
