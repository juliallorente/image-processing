import cv2
import numpy as np
import matplotlib.pyplot as plt

def destaca_regiao(taxa_roubo, imagem_mapa):
    # calculando o valor do pixel correspondente
    valor_pixel = int((taxa_roubo / 300.0) * 255)
    
    # criando uma máscara para o valor de fundo (branco)
    mascara_fundo = cv2.inRange(imagem_mapa, np.array([255, 255, 255]), np.array([255, 255, 255]))
    
    # criando uma máscara para as linhas de contorno (preto)
    mascara_contorno = cv2.inRange(imagem_mapa, np.array([0, 0, 0]), np.array([0, 0, 0]))
    
    # combinando as duas máscaras acima
    mascara_indesejada = cv2.bitwise_or(mascara_fundo, mascara_contorno)
    
    # invertendo a máscara indesejada para obter uma máscara das regiões de interesse
    mascara_rio = cv2.bitwise_not(mascara_indesejada)
    
    # convertendo a imagem colorida para uma imagem em escala de cinza
    imagem_cinza = cv2.cvtColor(imagem_mapa, cv2.COLOR_BGR2GRAY)
    
    # criando uma máscara onde a taxa de roubo é igual ao valor_pixel, e dentro das regiões de interesse
    mascara_taxa = cv2.inRange(imagem_cinza, valor_pixel - 5, valor_pixel + 5)
    mascara_final = cv2.bitwise_and(mascara_taxa, mascara_rio)
    
    # convertendo a imagem em escala de cinza para uma imagem colorida
    imagem_colorida = cv2.cvtColor(imagem_cinza, cv2.COLOR_GRAY2BGR)
    
    # destacando a região de interesse em vermelho
    imagem_colorida[np.where(mascara_final == 255)] = [0, 0, 255]
    
    # exibindo a imagem destacada usando Matplotlib
    plt.imshow(cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB))
    plt.show()

def identifica_e_destaca(imagem_mapa):
    imagem_cinza = cv2.cvtColor(imagem_mapa, cv2.COLOR_BGR2GRAY)
    tons_unicos = np.unique(imagem_cinza)
    print(f'Tons únicos: {tons_unicos}')
    
    for ton in tons_unicos:
        if ton not in [0, 255]:  # ignorando os tons de contorno e fundo
            taxa_roubo = (ton / 255.0) * 300
            print(f'Destacando região para a taxa de roubo: {taxa_roubo}')
            destaca_regiao(taxa_roubo, imagem_mapa)

# carregando a imagem do mapa
imagem_mapa_color = cv2.imread('taxaPerCapitaRouboCarros.png')

# identificando e destacando as regiões
identifica_e_destaca(imagem_mapa_color)
