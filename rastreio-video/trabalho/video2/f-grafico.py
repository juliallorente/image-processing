import matplotlib.pyplot as plt
import csv
import os

# métodos de template matching que foram testados
metodos = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# processar cada arquivo CSV e construir gráficos
for metodo in metodos:
    quadros = []
    min_vals = []
    max_vals = []

    # ler os dados do CSV
    with open(f'resultados_{metodo}.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        for row in reader:
            quadros.append(row[0])
            min_vals.append(float(row[1]))
            max_vals.append(float(row[2]))

    # construir o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot( min_vals, label='Min Val')
    plt.plot( max_vals, label='Max Val')
    plt.xlabel('Quadros')
    plt.ylabel('Resposta')
    plt.title(f'Resposta vs. Quadros ({metodo})')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvar o gráfico
    plt.savefig(f'grafico_{metodo}.png')

    # Exibir o gráfico (opcional)
    # plt.show()
