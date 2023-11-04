from tarefa import Imagem
import matplotlib.pyplot as plt


def salvar_histograma(hist_data, nome):
    # Cria um novo gráfico
    plt.figure()
    # Define os rótulos do eixo x como sendo os índices dos compartimentos
    x_labels = range(1, 11)
    # Cria o gráfico de barras
    plt.bar(x_labels, hist_data)
    # Define o título e os rótulos dos eixos
    plt.title('Histograma de Direção do Gradiente')
    plt.xlabel('Compartimento')
    plt.ylabel('Magnitude Acumulada')
    # Salva o gráfico como uma imagem
    plt.savefig(nome)
    plt.close()

    # Imprime os valores do histograma no console
    print(f"Valores do histograma para {nome.split('/')[-1]}:")
    for indice, valor in enumerate(hist_data, start=1):
        print(f"Compartimento {indice}: {valor}")
    print("-" * 40)

lua1_gray = Imagem('Imagens/Lua1_gray.jpg')
chessboard_inv = Imagem('Imagens/chessboard_inv.png')
img02 = Imagem('Imagens/img02.jpg')

print('Lua1_Gray')

lua1_gray.filtro_passa_baixa()

print('Sobel')
lua1_gray.sobel()
lua1_gray.magnitude_gradiente()
lua1_gray.direcao_gradiente()
lua1_gray.selecao_gradientes()
lua1_gray.bordas()
lua1_gray.salvar_imagem('Testes/Sobel/Lua1_gray.png')

# Gera e salva o histograma para lua1_gray com Sobel
hist_data = lua1_gray.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Sobel/Lua1_gray_histogram.png')

print('Prewitt')
lua1_gray.prewitt()
lua1_gray.magnitude_gradiente()
lua1_gray.direcao_gradiente()
lua1_gray.selecao_gradientes()
lua1_gray.bordas()
lua1_gray.salvar_imagem('Testes/Prewitt/Lua1_gray.png')

# Gera e salva o histograma para lua1_gray com Prewitt
hist_data = lua1_gray.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Prewitt/Lua1_gray_histogram.png')

print("Scharr")
lua1_gray.scharr()
lua1_gray.magnitude_gradiente()
lua1_gray.direcao_gradiente()
lua1_gray.selecao_gradientes()
lua1_gray.bordas()
lua1_gray.salvar_imagem('Testes/Scharr/Lua1_gray.png')

# Gera e salva o histograma para lua1_gray com Scharr
hist_data = lua1_gray.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Scharr/Lua1_gray_histogram.png')

print('Chessboard_inv')
# chessboard_inv.filtro_passa_baixa()

print('Sobel')
chessboard_inv.sobel()
chessboard_inv.magnitude_gradiente()
chessboard_inv.direcao_gradiente()
chessboard_inv.selecao_gradientes()
chessboard_inv.bordas()
chessboard_inv.salvar_imagem('Testes/Sobel/chessboard_inv.png')

# Gera e salva o histograma para chessboard_inv com Sobel
hist_data = chessboard_inv.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Sobel/chessboard_inv_histogram.png')

print('Prewitt')
chessboard_inv.prewitt()
chessboard_inv.magnitude_gradiente()
chessboard_inv.direcao_gradiente()
chessboard_inv.selecao_gradientes()
chessboard_inv.bordas()
chessboard_inv.salvar_imagem('Testes/Prewitt/chessboard_inv.png')

# Gera e salva o histograma para chessboard_inv com Prewitt
hist_data = chessboard_inv.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Prewitt/chessboard_inv_histogram.png')

print("Scharr")
chessboard_inv.scharr()
chessboard_inv.magnitude_gradiente()
chessboard_inv.direcao_gradiente()
chessboard_inv.selecao_gradientes()
chessboard_inv.bordas()
chessboard_inv.salvar_imagem('Testes/Scharr/chessboard_inv.png')

# Gera e salva o histograma para chessboard_inv com Scharr
hist_data = chessboard_inv.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Scharr/chessboard_inv_histogram.png')

print("img02")
# img02.filtro_passa_baixa()

print('Sobel')
img02.sobel()
img02.magnitude_gradiente()
img02.direcao_gradiente()
img02.selecao_gradientes()
img02.bordas()
img02.salvar_imagem('Testes/Sobel/img02.png')

# Gera e salva o histograma para img02 com Sobel
hist_data = img02.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Sobel/img02_histogram.png')

print('Prewitt')
img02.prewitt()
img02.magnitude_gradiente()
img02.direcao_gradiente()
img02.selecao_gradientes()
img02.bordas()
img02.salvar_imagem('Testes/Prewitt/img02.png')

# Gera e salva o histograma para img02 com Prewitt
hist_data = img02.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Prewitt/img02_histogram.png')

print("Scharr")
img02.scharr()
img02.magnitude_gradiente()
img02.direcao_gradiente()
img02.selecao_gradientes()
img02.bordas()
img02.salvar_imagem('Testes/Scharr/img02.png')

# Gera e salva o histograma para img02 com Scharr
hist_data = img02.histograma_direcao()
salvar_histograma(hist_data, 'Testes/Scharr/img02_histogram.png')




