import cv2
import numpy as np
import matplotlib.pyplot as plt

# lendo a imagem resultante
img1 = cv2.imread('output_imagem.jpg')

# convertendo a imagem para tons de cinza
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# criando/preenchendo vetor de frequencia para a cor de 0-255
h = np.zeros((256))
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        h[img2[i,j]] += 1

# aplicando algoritmo isodata para achar o limiar t
tprev = 0
t = 127
u1 = u2 = 0
while(abs(t-tprev)>=0.01):
    h1_sum = h2_sum =0
    for i in range(t+1):
       u1 += i*h[i]
       h1_sum += h[i]
    u1 /= h1_sum
    for i in range(t+1, 256):
       u2 += i*h[i]
       h2_sum += h[i]
    u2 /= h2_sum
    tprev = t
    t = round((u2+u1)/2)

# aplicação do limiar
_, img3 = cv2.threshold(img2, t, 255, cv2.THRESH_BINARY)

# convertendo BGR para RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# salva as imagens
cv2.imwrite('tons-cinza.jpg', img2)
cv2.imwrite('threshold.jpg', img3)


# mostrando as imagens usando matplotlib
plt.figure(figsize=(10,10))

plt.subplot(1,3,1)
plt.imshow(img1)
plt.title('Original')

plt.subplot(1,3,2)
plt.imshow(img2, cmap='gray')
plt.title('tons de cinza')

plt.subplot(1,3,3)
plt.imshow(img3, cmap='gray')
plt.title('threshold')

plt.show()
