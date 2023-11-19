import cv2
import numpy as np

#Kameram olmadığı İçin bir resim üzerinden kırmızı renkli nesne tespiti yaptım
#fakat kameradan görüntü okumak için aşağdaki fonksiyonu kulanabilirsiniz
'''
def Kameradan_Oku():
    
    kamera = cv2.VideoCapture(0)

    while True:
        ret, frame = kamera.read()

        if not ret:
            break
'''
def Kırmızıyı_Bul():

    resim = cv2.imread("resim.jpg") #görüntüyü okur

    hsv_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV) #görüntüyü RGB den HSV renk uzayına dönüştürür

    alt_kirmizi = np.array([0, 100, 100])    #HSV renk aralığında kırmızı renge denk
    ust_kirmizi = np.array([10, 255, 255])   #gelen renk aralığını belirler

    kirmizi_maske = cv2.inRange(hsv_resim, alt_kirmizi, ust_kirmizi)#kırmızı renge denk helen pikseleri belirler

    # Renkli nesneleri tespit etmek için bitwise AND işlemi uygula
    filtrelenmis_resim = cv2.bitwise_and(resim, resim, mask=kirmizi_maske)#mask edilecek yeri gösterir gerisini siyah yapar

    beyazlar = cv2.bitwise_not(kirmizi_maske)#kırmızı olmayan yerleri beyaz yapar
    filtrelenmis_resim[beyazlar == 255] = [255, 255, 255]

    cv2.imshow("Orijinal Resim", resim)             # Orijinal ve filtreli görüntüleri yan yana gösterirsd
    cv2.imshow("Filtreli Resim", filtrelenmis_resim)

    cv2.waitKey(0) #herhangi bir tuşa basıldığında pencereleri kapatır
    cv2.destroyAllWindows()


Kırmızıyı_Bul()