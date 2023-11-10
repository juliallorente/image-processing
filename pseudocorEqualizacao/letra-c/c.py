import cv2
import numpy as np

# função para equalização global de histograma
def global_histogram_equalization(img):
   # calculando o histograma
    hist, _ = np.histogram(img.flatten(), bins=256, range=[0,256])

    # normalizando o histograma
    hist_normalized = hist / float(img.size)

    # calculando a distribuição acumulada
    cdf = hist_normalized.cumsum()

    # a transformação é baseada na distribuição acumulada, escalada para o intervalo de intensidade de pixel [0, 255]
    transformation = (cdf * 255).astype(np.uint8)

    # aplicando a transformação para cada pixel na imagem
    img_eq = transformation[img]

    return img_eq

# função para equalização local de histograma
def local_histogram_equalization(img, window_size):
    # criação de uma borda refletida - para lidar com as bordas da imagem
    padded_img = cv2.copyMakeBorder(img, window_size//2, window_size//2, window_size//2, window_size//2, cv2.BORDER_REFLECT)
    local_eq_img = np.zeros_like(img)
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # obtendo a janela local centrada no pixel (i, j)
            local_window = padded_img[i:i+window_size, j:j+window_size]
            # calculando o histograma e o histograma cumulativo da janela local
            hist, bins = np.histogram(local_window, 256, [0,256])
            cdf = hist.cumsum()
            # normalizando o histograma cumulativo para o intervalo [0, 255]
            cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
            # remapeando o valor do pixel usando o histograma cumulativo normalizado
            local_eq_img[i, j] = cdf_normalized[img[i, j]]
    
    return local_eq_img

# carregadondo a imagem em escala de cinza
img = cv2.imread('XADREZ.png', cv2.IMREAD_GRAYSCALE)

# aplicando equalização global de histograma
global_eq = global_histogram_equalization(img)
cv2.imwrite('global_eq.png', global_eq) 

# aplicando equalização local de histograma com uma janela de tamanho 3x3
local_eq = local_histogram_equalization(img, 3)
cv2.imwrite('local_eq.png', local_eq) 

# repetindo o processo para a outra imagem
img_low = cv2.imread('xadrez_lowCont.png', cv2.IMREAD_GRAYSCALE)

global_eq_low = global_histogram_equalization(img_low)
cv2.imwrite('global_eq_low.png', global_eq_low)

local_eq_low = local_histogram_equalization(img_low, 3)
cv2.imwrite('local_eq_low.png', local_eq_low)
