#coding: utf-8
import cv2

imagem_carregada = cv2.imread("imagens/coins.jpg")
cv2.imshow("Imagem das moedas", imagem_carregada)
cv2.waitKey(0)
cv2.destroyAllWindows()
