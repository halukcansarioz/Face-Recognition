
# 👤 Face Recognition
### (OpenCV ve Python ile Yüz Tanıma Uygulaması)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)](#)
[![TensorFlow](https://img.shields.io/badge/dlib-008000?style=flat&logo=addthis&logoColor=white)](#)

Bu proje, Python ve OpenCV kullanarak görüntü ve gerçek zamanlı video akışlarında insan yüzlerini tespit edip tanımayı amaçlayan bir bilgisayarlı görü uygulamasıdır.

## 📚 İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [Teknoloji Yığını](#teknoloji-yığını)
- [Kurulum ve Kullanım](#kurulum-ve-kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Katkıda Bulunma](#katkıda-bulunma)
- [İletişim](#iletisim)
- [Lisans](#lisans)

---

## Proje Hakkında
Ankara Üniversitesi Bilgisayar Mühendisliği'nden mezun olduktan sonra kendimi geliştirme sürecimin bir parçası olan bu proje; yüz tespiti ve tanıma üzerine pratik bir bilgisayarlı görü uygulamasıdır. Haar Cascade sınıflandırıcıları ve LBPH (Local Binary Patterns Histogram) gibi yöntemleri kullanarak yüzleri algılar, eğitir ve tanır.

* **Geliştirici:** Haluk Can SARIÖZ
* **Tür:** Bilgisayarlı Görü / Yapay Zeka Uygulaması
* **Amaç:** OpenCV ve yüz tanıma tekniklerini uygulamalı olarak öğrenmek

---

## Özellikler
* **Yüz Tespiti:** Görüntü veya video karesi içindeki insan yüzlerini doğru şekilde konumlandırır.
* **Yüz Tanıma:** Bilinen yüz kodlamalarına dayanarak bireyleri tanımlar ve doğrular.
* **Gerçek Zamanlı İşleme:** Canlı web kamerası akışında çalışabilir.
* **Eğitici Modülü:** `trainer` klasörü ile sisteme yeni yüzler öğretme imkanı.
* **Sınırlayıcı Kutular:** Tanınan yüzlerin etrafına dikdörtgen ve isim etiketleri çizer.

---

## Teknoloji Yığını
| Katman | Teknoloji |
|--------|-----------|
| **Dil** | Python |
| **Bilgisayarlı Görü** | OpenCV (`cv2`) |
| **Makine Öğrenmesi** | `face_recognition` kütüphanesi (dlib tabanlı), NumPy |
| **Sınıflandırıcı** | Haar Cascade, LBPH |
| **Versiyon Kontrol** | Git & GitHub |

---

## Kurulum ve Kullanım

### Ön Gereksinimler
* [Python 3.x](https://www.python.org/downloads/)
* Git
* C++ derleyicisi (bazı işletim sistemlerinde `dlib`'in doğru şekilde derlenmesi için gerekebilir)

### Kurulum Adımları

**1. Depoyu klonlayın:**
```bash
git clone https://github.com/halukcansarioz/Face-Recognition.git
```

**2. Proje dizinine gidin:**
```bash
cd Face-Recognition
```

**3. Sanal ortam oluşturun (önerilir):**
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

**4. Gerekli kütüphaneleri yükleyin:**
```bash
pip install opencv-python face-recognition numpy
```

**5. Uygulamayı çalıştırın:**

Yüz tanıma taraması için:
```bash
python Tarama.py
```

Yeni yüz görüntüsü almak için:
```bash
python Resim_Alma.py
```

Eğitim değerlendirmesi için:
```bash
python degerlendirme.py
```

---

## Proje Yapısı
```text
Face-Recognition/
├── .idea/                 # IDE yapılandırma dosyaları
├── Cascade/               # Haar Cascade XML dosyaları
├── trainer/               # Eğitilmiş model dosyaları
├── venv/                  # Sanal ortam (opsiyonel)
├── Resim_Alma.py          # Yeni yüz görüntüsü yakalama betiği
├── Tarama.py              # Yüz tanıma tarama betiği
├── degerlendirme.py       # Model değerlendirme betiği
├── .gitattributes         # Git yapılandırma dosyası
└── README.md              # Proje dökümantasyonu
```

---

## Katkıda Bulunma
Katkılarınız, hata bildirimleriniz ve özellik istekleriniz memnuniyetle karşılanır!

1. Bu depoyu **Fork**'layın.
2. Bir **Branch** oluşturun (`git checkout -b feature/YeniOzellik`).
3. Değişikliklerinizi **Commit** edin (`git commit -m 'Ekleme: Yeni özellik'`).
4. Kodlarınızı **Push**'layın (`git push origin feature/YeniOzellik`).
5. Bir **Pull Request** açın.

---

<a name="iletisim"></a>
## İletişim
**Haluk Can Sarıöz**
- GitHub: [@halukcansarioz](https://github.com/halukcansarioz)
- E-posta: [halukcansarioz19@gmail.com](mailto:halukcansarioz19@gmail.com)
- LinkedIn: [Haluk Can Sarıöz](https://www.linkedin.com/in/halukcansarioz)

---

*Bu bilgisayarlı görü projesini faydalı bulduysanız ⭐ vermeyi unutmayın!*

---

## Lisans
Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
