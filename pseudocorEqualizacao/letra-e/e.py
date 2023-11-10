import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, exposure

# função para equalizar os canais RGB de uma imagem
def equalize_rgb_image(img):
    r, g, b = cv2.split(img)  # separando os canais da imagem
    r_eq = cv2.equalizeHist(r)  # equaliza o canal R
    g_eq = cv2.equalizeHist(g)  # equaliza o canal G
    b_eq = cv2.equalizeHist(b)  # equaliza o canal B
    return cv2.merge((r_eq, g_eq, b_eq))  # junta os canais equalizados

# função para equalizar o canal Y no espaço YIQ
def equalize_y_channel(yiq_img):
    y, i, q = cv2.split(yiq_img)  # separa os canais da imagem YIQ
    y_eq = exposure.equalize_hist(y)  # equaliza o canal Y
    return cv2.merge((y_eq, i, q))  # junta os canais com Y equalizado

# carregando as imagens
img_outono = cv2.imread('outono_LC.png')
img_predios = cv2.imread('predios.jpeg')

# convertendo as imagens carregadas para o espaço de cores RGB
img_outono_rgb = cv2.cvtColor(img_outono, cv2.COLOR_BGR2RGB)
img_predios_rgb = cv2.cvtColor(img_predios, cv2.COLOR_BGR2RGB)

# equalizando os canais RGB diretamente
equalized_rgb_outono = equalize_rgb_image(img_outono_rgb)
equalized_rgb_predios = equalize_rgb_image(img_predios_rgb)

# convertendo as imagens equalizadas para o espaço YIQ
yiq_outono = color.rgb2yiq(equalized_rgb_outono)
yiq_predios = color.rgb2yiq(equalized_rgb_predios)

# equalizando apenas o canal Y no espaço YIQ
equalized_yiq_outono = equalize_y_channel(yiq_outono)
equalized_yiq_predios = equalize_y_channel(yiq_predios)

# convertendo as imagens de volta para o espaço RGB
equalized_rgb_outono_final = color.yiq2rgb(equalized_yiq_outono)
equalized_rgb_predios_final = color.yiq2rgb(equalized_yiq_predios)

# mostrando as imagens resultantes
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(equalized_rgb_outono)
plt.title("Outono Equalizado (RGB)")

plt.subplot(2, 2, 2)
plt.imshow(equalized_rgb_predios)
plt.title("Predios Equalizado (RGB)")

plt.subplot(2, 2, 3)
plt.imshow(equalized_rgb_outono_final)
plt.title("Outono Equalizado (RGB convertida de YIQ)")

plt.subplot(2, 2, 4)
plt.imshow(equalized_rgb_predios_final)
plt.title("Predios Equalizado (RGB convertida de YIQ)")

plt.tight_layout()
plt.show()
