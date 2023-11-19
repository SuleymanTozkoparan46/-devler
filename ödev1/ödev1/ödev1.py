import cv2
import numpy as np
import matplotlib.pyplot as plt

# Gri seviye görüntüyü yükle          # Görüntüyü gri seviyeye çevir
image = cv2.imread('gri_goruntu.png', cv2.IMREAD_GRAYSCALE)

# Histogramı hesaplamak için bir dizi oluştur
histogram = np.zeros(256, dtype=int)

# Görüntüdeki her pikseli gez
height, width = image.shape
for i in range(height):
    for j in range(width):
        pixel_value = image[i, j]
        histogram[pixel_value] += 1

# Histogramı çiz
plt.bar(np.arange(256), histogram, color='gray')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')
plt.title('Histogram')
plt.show()