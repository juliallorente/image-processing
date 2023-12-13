import cv2
import os

import os
print(os.getcwd())


# função para redimensionar o template
def redimensionar_template(template, escala):
    # impedir que a escala seja menor que um certo limite (por exemplo, 0.2)
    escala = max(escala, 0.2)
    largura = int(template.shape[1] * escala)
    altura = int(template.shape[0] * escala)
    dimensoes = (largura, altura)
    return cv2.resize(template, dimensoes, interpolation=cv2.INTER_AREA)

template_path = 'video2/template.jpg'  # Caminho atualizado
template_original = cv2.imread(template_path, 0)


# verificar se o template foi carregado corretamente
if template_original is None:
    raise FileNotFoundError(f"Não foi possível carregar a imagem do template em '{template_path}'. Verifique o caminho e tente novamente.")
w, h = template_original.shape[::-1]

# processar cada quadro
for indice, nome_quadro in enumerate(sorted(os.listdir('video2/frames_cinza'))):
    frame = cv2.imread(os.path.join('video2/frames_cinza', nome_quadro), 0)
    
    # extrair o número do quadro a partir do nome do arquivo
    numero_do_quadro = int(nome_quadro.split('_')[-1].split('.')[0])
    # ajustar a taxa de diminuição e garantir que a escala não seja negativa
    fator_de_diminuicao = 0.0025  # valor reduzido para diminuir a escala mais lentamente
    escala = max(1 - (fator_de_diminuicao * numero_do_quadro), 0.2)
    template = redimensionar_template(template_original, escala)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(frame, template, cv2.TM_CCORR_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    # no método TM_CCORR_NORMED, valores maiores indicam melhores correspondências
    if max_val > 0.8:  # ajuste este limiar conforme necessário
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(frame, top_left, bottom_right, 255, 2)
        cv2.imwrite(os.path.join('video2/frames_rastreio_ccorr_normed', nome_quadro), frame)
