#coding: utf-8
'''
*** Objetivo:
Gerar um histograma de uma imagem: sem bibliotecas

*** Funções:
PrettyPrinter(indent=4) = configura o pprint para exibir identação de 4 espaços
set_printoptions(threshold=np.nan) = seta o threshold da exibição dos arrays
ravel() = retorna os valores da imagem em array
hist() = função do matplotlib para plotar um histograma
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem_carregada = cv2.imread("imagens/Figura3.tif", 0)
plt.hist(imagem_carregada.ravel(), 256, [0, 256])
cv2.imshow("Imagem Original", imagem_carregada)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
