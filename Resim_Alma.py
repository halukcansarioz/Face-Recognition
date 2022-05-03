import cv2

Sayaç = 0
Kamera = cv2.VideoCapture(0)
Yuz_Tanıma = cv2.CascadeClassifier("Cascade/haarcascade_frontalface_default.xml")
Yuz_Kimlik = input('\nNumaranızı giriniz: ')
print("\n Yüz yakalama başlayacak. Kameraya bak:")

while True:
    ret, Resim = Kamera.read()
    Resim = cv2.flip(Resim, 1)
    Gri = cv2.cvtColor(Resim, cv2.COLOR_BGR2GRAY)
    Yuzler = Yuz_Tanıma.detectMultiScale(Gri, 1.3, 5)

    for (x, y, w, h) in Yuzler:
        Sayaç += 1
        cv2.rectangle(Resim, (x, y), (x + w, y + h), (255, 0, 0), 5)
        cv2.imwrite("Veri/User." + str(Yuz_Kimlik) + '.' + str(Sayaç) + ".jpg", Gri[y:y + h, x:x + w])
        cv2.imshow('image', Resim)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif Sayaç >=60:
        break

Kamera.release()
cv2.destroyAllWindows()
