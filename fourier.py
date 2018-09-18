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

def fft_inversa(im):
    f = im.copy()
    f = np.fft.ifftshift(f)
    f = np.fft.ifft2(f)
    f = np.abs(f)
    return f

def filtro_pb(im, raio):
    f = im.copy()
    cx = im.shape[0]/2
    cy = im.shape[1]/2
    f[:,:] = 1 # Substitui os valores dos pixels por 1
    f[int(cx-raio):int(cx+raio), int(cy-raio):int(cy+raio)] = 0
    return f

img_resultado = fft_inversa(fft_spectrum(imagem)*filtro_pb(imagem,10))

plt.subplot(121),plt.imshow(imagem, cmap = 'gray')
plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_resultado, cmap = 'gray')
plt.title('Imagem - Transformada de Fourie'), plt.xticks([]), plt.yticks([])
plt.show()
