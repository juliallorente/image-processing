import cv2
import numpy as np
import math

class Imagem:
    def __init__(self, caminho):
        # Lê a imagem em escala de cinza
        self.imagem = cv2.imread(caminho, 2)
        # Define as dimensões da imagem
        self.altura = len(self.imagem)
        self.largura = len(self.imagem[0])
        self.tam_conjuntos = []
        
    def salvar_imagem(self, nome):
            # Salva a imagem original e as derivadas dela em diferentes arquivos
            cv2.imwrite(nome, self.imagem)
            cv2.imwrite(nome.replace('.png', '_Gx.png'), self.gx)
            cv2.imwrite(nome.replace('.png', '_Gy.png'), self.gy)
            cv2.imwrite(nome.replace('.png', '_magnitude.png'), self.imagem_magnitude)
            cv2.imwrite(nome.replace('.png', '_bordas.png'), self.imagem_bordas)
            if not cv2.imwrite(nome, self.imagem):
                print(f"Erro ao salvar a imagem {nome}")
        
            if not cv2.imwrite(nome.replace('.png', '_Gx.png'), self.gx):
                print(f"Erro ao salvar a imagem {nome.replace('.png', '_Gx.png')}")
            
            if not cv2.imwrite(nome.replace('.png', '_Gy.png'), self.gy):
                print(f"Erro ao salvar a imagem {nome.replace('.png', '_Gy.png')}")
            
            if not cv2.imwrite(nome.replace('.png', '_magnitude.png'), self.imagem_magnitude):
                print(f"Erro ao salvar a imagem {nome.replace('.png', '_magnitude.png')}")
            
            if not cv2.imwrite(nome.replace('.png', '_bordas.png'), self.imagem_bordas):
                print(f"Erro ao salvar a imagem {nome.replace('.png', '_bordas.png')}")

    def median(self, vet): # Calcula a mediana de um vetor 
        vet = sorted(vet)
        n = len(vet)
        # print(n)
        if n % 2 == 0:
            return (int(vet[n//2])+int(vet[int(n//2)-1]))//2
        return vet[n//2]

    def valido(self, px, py): # Verifica se as coordenadas estão dentro dos limites da imagem
        return px >= 0 and py >= 0 and px < self.altura and py < self.largura

    # 1) pré-filtragem
    # Aplica um filtro passa-baixa usando mediana
    def filtro_passa_baixa(self): 
        aux_img = self.imagem.copy()
        for l in range(0, self.altura):
            for c in range(0, self.largura):
                vet = []
                for i in range(-1,2):
                    for j in range(-1,2):
                        if self.valido(l+i, c+j):
                            vet.append(self.imagem[l+i][c+j])
                aux_img[l][c] = self.median(vet)
        self.imagem = aux_img
        
    # 2) aplicação do filtro derivativo
    # Aplica um filtro derivativo usando os operadores fornecidos
    def filtro_derivativo(self, operador_x, operador_y):
        img_aux = np.zeros((self.altura+2, self.largura+2), np.uint8)
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                img_aux[i][j] = self.imagem[i][j]
        
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                janela = img_aux[i:i+3, j:j+3]
                self.gx[i][j] = np.abs(np.sum(operador_x @ janela))
                self.gy[i][j] = np.abs(np.sum(janela @ operador_y))

    # 3) determinação da magnitude do gradiente (M)
        # calcula a magnitude do gradiente da imagem
    def magnitude_gradiente(self):
        self.imagem_magnitude = self.imagem.copy()
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                self.imagem_magnitude[i][j] = (self.gy[i][j]**2 + self.gx[i][j]**2)**(1/2.0)

    # 4) determinação da direção do gradiente (D)
    # calcula a direção do gradiente da imagem em graus
    def direcao_gradiente(self):
        self.matriz_direcao = []
        for i in range(0, self.altura):
            self.matriz_direcao.append([0]*self.largura)
        eps = 10**(-8)
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                self.matriz_direcao[i][j] = math.degrees(math.atan2(self.gy[i][j],self.gx[i][j]+eps))
                
    # 5) seleção dos máximos locais (supressão dos não máximos)
    # realiza a supressão não máxima no gradiente da imagem
    def selecao_gradientes(self): 
        self.max_locais = []
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                x = (0,0)
                y = (0,0)
                d_px = self.matriz_direcao[i][j]

                if -180 <= d_px and d_px <= -157.5:
                    y = (i,j-1)
                    x = (i,j+1)
                elif -157.5 < d_px and d_px <= -112.5:
                    y = (i+1,j-1)
                    x = (i-1,j+1)
                elif -112.5 < d_px and d_px <= -67.5:
                    y = (i+1,j)
                    x = (i-1,j)
                elif -67.5 < d_px and d_px <= -22.5:
                    y = (i+1,j+1)
                    x = (i-1,j-1)
                elif -22.5 < d_px and d_px <= 22.5:
                    y = (i,j+1)
                    x = (i,j-1)
                elif 22.5 < d_px and d_px <= 67.5:
                    y = (i-1,j+1)
                    x = (i+1,j-1)
                elif 67.5 < d_px and d_px <= 112.5:
                    y = (i-1,j)
                    x = (i+1,j)
                elif 112.5 < d_px and d_px <= 157.5:
                    y = (i-1,j-1)
                    x = (i+1,j+1)
                else:
                    y = (i,j-1)
                    x = (i,j+1)
                
                if self.valido(x[0], x[1]) and self.valido(y[0], y[1]):
                    mag_ij = self.imagem_magnitude[i][j]
                    mag_x = self.imagem_magnitude[x[0]][x[1]]
                    mag_y = self.imagem_magnitude[y[0]][y[1]]

                    if (mag_ij > mag_x and mag_ij > mag_y):
                        self.max_locais.append((i,j))

    def bordas(self): # Marca as bordas da imagem com base nos máximos locais
        self.imagem_bordas = self.imagem.copy()
        for i in range(0, self.altura):
            for j in range(0, self.largura):
                self.imagem_bordas[i][j] = 0
        for (i,j) in self.max_locais:
            self.imagem_bordas[i][j] = 255
                    
    # Aplica o filtro Sobel na imagem
    def sobel(self): 
        self.gx = self.imagem.copy()
        self.gy = self.imagem.copy()
        operador_x = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])

        operador_y = np.array([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ])

        self.filtro_derivativo(operador_x, operador_y)

    # Aplica o filtro Prewitt na imagem
    def prewitt(self): 
        self.gx = self.imagem.copy()
        self.gy = self.imagem.copy()
        operador_x = np.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ])

        operador_y = np.array([
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1]
        ])

        self.filtro_derivativo(operador_x, operador_y)

    # Aplica o filtro Scharr na imagem
    def scharr(self):  
        self.gx = self.imagem.copy()
        self.gy = self.imagem.copy()
        operador_x = np.array([
            [-3, 0, 3],
            [-10, 0, 10],
            [-3, 0, 3]
        ])

        operador_y = np.array([
            [-3, -10, -3],
            [0, 0, 0],
            [3, 10, 3]
        ])

        self.filtro_derivativo(operador_x, operador_y)
        
        
    # tarefa 2 - histograma
    def histograma_direcao(self):
        # Cria um histograma com 10 compartimentos
        histograma = [0] * 10
        # Determina o tamanho de cada compartimento em graus
        bucket_size = 360.0 / 10  # 360 graus dividido por 10 compartimentos

        # Itera sobre os máximos locais (gradientes fortes) que foram determinados
        for (i, j) in self.max_locais:
            # Obtém a direção e magnitude do gradiente
            direcao = self.matriz_direcao[i][j]
            magnitude = self.imagem_magnitude[i][j]

            # Determina os compartimentos no histograma
            primeiro_bucket = int(direcao // bucket_size)
            segundo_bucket = (primeiro_bucket + 1) % 10

            # Calcula a fração da direção no primeiro compartimento
            frac = (direcao % bucket_size) / bucket_size

            # Distribui a magnitude entre os compartimentos
            histograma[primeiro_bucket] += magnitude * (1 - frac)
            histograma[segundo_bucket] += magnitude * frac

        return histograma

    