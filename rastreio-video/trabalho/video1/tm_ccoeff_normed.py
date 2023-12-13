import cv2
import os

# função para redimensionar o template
def redimensionar_template(template, escala):
    # impedir que a escala seja menor que um certo limite (por exemplo, 0.2)
    escala = max(escala, 0.2)
    largura = int(template.shape[1] * escala)
    altura = int(template.shape[0] * escala)
    dimensoes = (largura, altura)
    return cv2.resize(template, dimensoes, interpolation=cv2.INTER_AREA)

# carregar o template original
template_original = cv2.imread('video1/template.jpg', 0)
w, h = template_original.shape[::-1]

# processar cada quadro
for indice, nome_quadro in enumerate(sorted(os.listdir('video1/frames_cinza'))):
    frame = cv2.imread(os.path.join('video1/frames_cinza', nome_quadro), 0)
    
    # extrair o número do quadro a partir do nome do arquivo
    numero_do_quadro = int(nome_quadro.split('_')[-1].split('.')[0])
    # ajustar a taxa de diminuição e garantir que a escala não seja negativa
    fator_de_diminuicao = 0.005  # valor reduzido para diminuir a escala mais lentamente
    escala = max(1 - (fator_de_diminuicao * numero_do_quadro), 0.2)
    template = redimensionar_template(template_original, escala)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    if max_val > 0.8:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(frame, top_left, bottom_right, 255, 2)
        cv2.imwrite(os.path.join('video1/frames_rastreio_ccoeff_normed', nome_quadro), frame)
