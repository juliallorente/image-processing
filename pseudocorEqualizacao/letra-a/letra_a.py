import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np
from PIL import Image

# carregando a imagem em tons de cinza
image_path = 'taxaPerCapitaRouboCarros.png'
gray_image = Image.open(image_path)

# convertendo a imagem em tons de cinza para uma matriz NumPy
gray_array = np.array(gray_image)

# identificando onde a imagem é branca (assumindo que branco é representado por 255)
is_white = gray_array == 255

# normalizando os valores de pixel para o intervalo [0, 1], exceto para os pixels brancos
normalized_array = np.where(is_white, 1, gray_array / 255.0)

# escolhendo um mapa de cores (azul para valores baixos, vermelho para valores altos)
colormap = plt.cm.get_cmap("coolwarm")

# aplicando o mapa de cores
colored_array = colormap(normalized_array)

# fundo branco
colored_array[is_white] = [1, 1, 1, 1]  # Branco em RGBA

# convertendo a matriz colorida de volta para uma imagem
colored_image = Image.fromarray((colored_array[:, :, :3] * 255).astype(np.uint8))

# salvando a imagem colorida
colored_image.save('colored_mapa_brasil.png')

# mostrando a imagem
colored_image.show()