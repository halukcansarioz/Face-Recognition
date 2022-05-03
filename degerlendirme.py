import cv2
import numpy as np
from PIL import Image
import os

Tanıyıcı = cv2.face.LBPHFaceRecognizer_create()
Detector = cv2.CascadeClassifier("Cascade/haarcascade_frontalface_default.xml")
Yol = 'Veri'

def Goruntu_Alma(Yol):
    Resim_Yolu = [os.path.join(Yol, f) for f in os.listdir(Yol)]
    Resim_Ornek = []
    Resımler = []
    for Resim_Yol in Resim_Yolu:
        PIL_Resim = Image.open(Resim_Yol).convert('L')
        Resim_Dizi = np.array(PIL_Resim, 'uint8')
        Kimlik = int(os.path.split(Resim_Yol)[-1].split(".")[2])
        Yüzler = Detector.detectMultiScale(Resim_Dizi)
        for (x, y, w, h) in Yüzler:
            Resim_Ornek.append(Resim_Dizi[y:y + h, x:x + w])
            Resımler.append(Kimlik)
    return Resim_Ornek, Resımler

print("\nYüzler taranıyor.Birkaç saniye sürecek bekleyiniz")
Yuzler, Resımler = Goruntu_Alma(Yol)
Tanıyıcı.train(Yuzler, np.array(Resımler))
Tanıyıcı.write('trainer/trainer.yml')
print("\nTarama tamamlandı")


cv2.waitKey(0)
cv2.destroyAllWindows()