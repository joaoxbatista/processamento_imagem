#coding: utf-8
'''
*** Objetivo:
Gerar a imagem com cores invertidas

*** Funções:
'''
import cv2

imagem_carregada = cv2.imread("imagens/coins.jpg", 0)
imagem_carregada_negativa = (255 - imagem_carregada)

cv2.imshow("Imagem das moedas", imagem_carregada)
cv2.waitKey(0)
cv2.imshow("Imagem das moedas negativas", imagem_carregada_negativa)
cv2.waitKey(0)
