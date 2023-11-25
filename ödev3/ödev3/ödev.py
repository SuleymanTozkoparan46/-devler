import cv2
import numpy as np

def say_pirinc_taneleri(resim_yolu):
    # Resmi oku
    resim = cv2.imread(resim_yolu)


    # Gri tonlamaya çevir
    gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

    # Eşikleme uygula
    _, esik_resim = cv2.threshold(gri_resim, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow("esik_resim",esik_resim)
    cv2.waitKey()
    # Bağlantılı bileşenleri etiketleme
    _, etiket_resim = cv2.connectedComponents(esik_resim)

    # Pirinç tanelerini say
    pirinc_tane_sayisi = etiket_resim.max()

    return pirinc_tane_sayisi

# Örnek: Resimdeki pirinç tanelerini say
resim_yolu = "pirinc_resmi.jpg"  # Kullanacağınız resmin yolunu belirtin
tane_sayisi = say_pirinc_taneleri(resim_yolu)

print(f"Resimdeki pirinç tanelerinin sayısı: {tane_sayisi}")
