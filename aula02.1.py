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

imagem_carregada = cv2.imread("imagens/Figura3.tif", 0)
quantidade = [0] * 256
histograma = {}


for pixel in imagem_carregada.ravel():
    quantidade[pixel] = quantidade[pixel] + 1

print("Histograma da Imagem: (tom -> quantidade de pixels)")
for i in range(0, 256):
    print("(tom:%i -> quantidade:%i)" % (i, quantidade[i]))
