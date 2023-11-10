import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_matching(img, specified_histogram):
    # calculando o histograma cumulativo da imagem original
    hist, bins = np.histogram(img.flatten(), 256, [0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf / float(cdf.max())  # normalizando para o intervalo [0,1]

    # calculando o histograma cumulativo do histograma especificado
    cdf_specified = specified_histogram.cumsum()
    cdf_specified_normalized = cdf_specified / float(cdf_specified.max())  # normalizando para o intervalo [0,1]

    # inicializando o mapeamento de transferência
    transfer_map = np.zeros(256)

    # calculando o mapeamento de transferência
    for i in range(256):
        # encontrando o valor de mapeamento que minimiza a diferença entre os histogramas
        differences = np.abs(cdf_normalized[i] - cdf_specified_normalized)
        transfer_map[i] = np.argmin(differences)

    # aplicando o mapeamento de transferência
    img_matched = transfer_map[img]

    return img_matched.astype(np.uint8)

# carregando a imagem
img = cv2.imread('XADREZ.png', 0)

# verificando se a imagem foi carregada corretamente
if img is None:
    print("Erro: Não foi possível carregar a imagem.")
    exit()

# histograma especificado
specified_histogram = np.ones(256) * (1.0 / 256.0)

# especificação de histograma
img_matched = histogram_matching(img, specified_histogram)

# Mostrar a imagem original e a imagem especificada
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(img_matched, cmap='gray')
plt.title('Matched Image')

# histogramas
plt.subplot(2, 2, 3)
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram of Original Image')

plt.subplot(2, 2, 4)
plt.hist(img_matched.ravel(),256,[0,256])
plt.title('Histogram of Matched Image')

plt.tight_layout()
plt.show()
