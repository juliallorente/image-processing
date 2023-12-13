import cv2
import os
import csv

# carregar o template
template = cv2.imread('template.jpg', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

# métodos de template matching a serem testados
metodos = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# lista de nomes dos arquivos dos quadros
lista_de_quadros = sorted([f for f in os.listdir('frames_cinza') if f.endswith('.jpg')])

# processar cada quadro com cada método e salvar os resultados
for metodo in metodos:
    resultados = []
    for nome_quadro in lista_de_quadros:
        quadro = cv2.imread(f'frames_cinza/{nome_quadro}', cv2.IMREAD_GRAYSCALE)

        # aplicar template matching
        metodo_eval = eval(metodo)
        res = cv2.matchTemplate(quadro, template, metodo_eval)
        min_val, max_val, _, _ = cv2.minMaxLoc(res)

        # adicionar os resultados à lista
        resultados.append([nome_quadro, min_val, max_val])

    # salvar os resultados em um arquivo CSV
    with open(f'resultados_{metodo}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Quadro (imagem)', 'min_val', 'max_val'])
        writer.writerows(resultados)
