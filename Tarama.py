import cv2

Kimlik = 0
İsimler = ['Haluk']
Font = cv2.FONT_HERSHEY_SIMPLEX
Recognizer = cv2.face.LBPHFaceRecognizer_create()
Recognizer.read('trainer/trainer.yml')
Face_Cascade = cv2.CascadeClassifier("Cascade/haarcascade_frontalface_default.xml")

Kamera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
Kamera.set(4, 480)
Kamera.set(3, 640)

Minimum_H = 0.1 * Kamera.get(4)
Minimum_W = 0.1 * Kamera.get(3)

while True:
    ret, Resim = Kamera.read()
    Resim = cv2.flip(Resim, 1)
    Gri = cv2.cvtColor(Resim, cv2.COLOR_BGR2GRAY)
    Yuzler = Face_Cascade.detectMultiScale(
        Gri,
        scaleFactor=1.5,
        minNeighbors=4,
        minSize=(int(Minimum_W), int(Minimum_H))
    )
    for (x, y, w, h) in Yuzler:
        cv2.rectangle(Resim, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id, Yüzde = Recognizer.predict(Gri[y:y + h, x:x + w])
        if Yüzde < 60:
            id = İsimler[0]
        else:
            id = "bilinmiyor"

            def Bulurlama(Resim_Gri, Renk):

                Yüzler = Face_Cascade.detectMultiScale(Gri, scaleFactor=1.5, minNeighbors=4, minSize=(int(Minimum_W), int(Minimum_H)), )

                for (y, x, w, h) in Yüzler:
                    Roi_Renk = Renk[y:y + h, x:x + w]

                    frames = cv2.GaussianBlur(Roi_Renk, (101, 101), 0)

                    Renk[y:y + h, x:x + w] = frames

                return Renk

            frame = Bulurlama(Gri, Resim)

        cv2.putText(Resim, str(id), (x + 5, y - 5), Font, 1, (255, 255, 255), 2)

    cv2.imshow('Kamera', Resim)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Kamera.release()
cv2.destroyAllWindows()
