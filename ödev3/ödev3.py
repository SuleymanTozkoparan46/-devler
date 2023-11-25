import cv2

def say_pirinc_taneleri(resim_yolu):
    resim = cv2.imread(resim_yolu, cv2.IMREAD_GRAYSCALE)
    yeni_boyut = (600, 600)
    boyutlandırılmıs_resim = cv2.resize(resim,yeni_boyut)
    cv2.imshow("Pirinc resim", boyutlandırılmıs_resim)

    _, esik_resim = cv2.threshold(resim, 100, 255, cv2.THRESH_BINARY)
    boyutlandırılmıs_eşik_resim = cv2.resize(esik_resim,yeni_boyut)
    cv2.imshow("esik resim",boyutlandırılmıs_eşik_resim)

    _, etiket_resim = cv2.connectedComponents(esik_resim)

    pirinc_tane_sayisi = etiket_resim.max()

    return pirinc_tane_sayisi

resim_yolu = "pirinc_resmi.jpg"
tane_sayisi = say_pirinc_taneleri(resim_yolu)

print(f"Resimdeki pirinç tanelerinin sayısı: {tane_sayisi}")
cv2.waitKey(0)