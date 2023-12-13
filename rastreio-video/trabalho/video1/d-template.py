import cv2

# carregar a primeira imagem
primeira_imagem = cv2.imread('video1/frames_cinza/img_frame_00000.jpg', cv2.IMREAD_GRAYSCALE)

# coordenadas e o tamanho do template
x, y, largura, altura = 10, 450, 500, 135

# cortar a região do template
template = primeira_imagem[y:y+altura, x:x+largura]

# template cortado p/ verificação
cv2.imshow('Template', template)
cv2.waitKey(0)
cv2.destroyAllWindows()

# salvar o template
cv2.imwrite('template.jpg', template)
