import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('imagens/Figura1.jpg', 0)

def negativo(img):
    img_cp = img.copy()
    img_cp = 255 - img_cp
    return img_cp

def fft_spectrum(im):
    f = im.copy()
    f = np.fft.fft2(f)
    f = np.fft.fftshift(f)
    return f

def fft_spectrum_mag(im):
    f = im.copy()
    f = 20 * np.log(np.abs(f))
    return f

'''
Função para trazer a imagem de volta do domínio de frequencia
'''
def fft_inversa(im):
    f = im.copy()
    f = np.fft.ifftshift(f)
    f = np.fft.ifft2(f)
    f = np.abs(f)
    return f

'''
Função para o filtro passa baixa
'''
def filtro_pb(im, raio):
    f = im.copy()
    cx = im.shape[0]/2
    cy = im.shape[1]/2
    f[:,:] = 1 # Substitui os valores dos pixels por 1
    f[int(cx-raio):int(cx+raio), int(cy-raio):int(cy+raio)] = 0
    return f

def filtro_covolucao(img, masc):
    kernel = np.ones((masc,masc),np.float32)/25
    img_result = cv2.filter2D(img,-1,kernel)
    return img_result

'''
Obtem as imagens de resultado
'''
img_magnitude = fft_spectrum_mag(fft_spectrum(imagem))
img_resultado = fft_inversa(fft_spectrum(imagem)*filtro_pb(imagem,6))
img_resultado_covolucao = filtro_covolucao(fft_inversa(fft_spectrum(imagem)*filtro_pb(imagem,6)), 10)


plt.subplot(121),plt.imshow(img_resultado, cmap = 'gray')
plt.title('Imagem após a reconstrução'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_resultado_covolucao, cmap = 'gray')
plt.title('Imagem após a covoluçao'), plt.xticks([]), plt.yticks([])
plt.show()
