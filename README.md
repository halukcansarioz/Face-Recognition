# 👤 Face Recognition
### (Face Recognition Application with OpenCV and Python)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)](#)
[![dlib](https://img.shields.io/badge/dlib-008000?style=flat&logo=addthis&logoColor=white)](#)

This project is a computer vision application that aims to detect and recognize human faces in images and real‑time video streams using Python and OpenCV.

## 📚 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Usage](#installation--usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

---

## About the Project
As part of my continuous self‑improvement journey after graduating from Ankara University Computer Engineering, this project is a practical computer vision application focused on face detection and recognition. It detects, trains on, and recognizes faces using methods such as Haar Cascade classifiers and LBPH (Local Binary Patterns Histogram).

- **Developer:** Haluk Can SARIÖZ
- **Type:** Computer Vision / Artificial Intelligence Application
- **Purpose:** Hands‑on learning of OpenCV and face recognition techniques

---

## Features
- **Face Detection** – Accurately locates human faces within an image or video frame.
- **Face Recognition** – Identifies and verifies individuals based on known face encodings.
- **Real‑Time Processing** – Can operate on a live webcam stream.
- **Training Module** – The `trainer` folder provides the ability to teach new faces to the system.
- **Bounding Boxes** – Draws rectangles and name labels around recognized faces.

---

## Tech Stack

| Layer | Technology |
|:-------|:-----------|
| **Language** | Python |
| **Computer Vision** | OpenCV (`cv2`) |
| **Machine Learning** | `face_recognition` library (dlib‑based), NumPy |
| **Classifier** | Haar Cascade, LBPH |
| **Version Control** | Git & GitHub |

---

## Installation & Usage

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- Git
- C++ compiler (may be required on some operating systems for `dlib` to compile correctly)

### Installation Steps

**1. Clone the repository:**
```bash
git clone https://github.com/halukcansarioz/Face-Recognition.git
```

**2. Navigate to the project directory:**
```bash
cd Face-Recognition
```

**3. Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

**4. Install the required libraries:**
```bash
pip install opencv-python face-recognition numpy
```

**5. Run the application:**

For face recognition scanning:
```bash
python Tarama.py
```

To capture a new face image:
```bash
python Resim_Alma.py
```

For training evaluation:
```bash
python degerlendirme.py
```

---

## Project Structure
```text
Face-Recognition/
├── .idea/                 # IDE configuration files
├── Cascade/               # Haar Cascade XML files
├── trainer/               # Trained model files
├── venv/                  # Virtual environment (optional)
├── Resim_Alma.py          # New face image capture script
├── Tarama.py              # Face recognition scanning script
├── degerlendirme.py       # Model evaluation script
├── .gitattributes         # Git configuration file
└── README.md              # Project documentation
```

---

## Contributing
Contributions, bug reports, and feature requests are welcome!

1. **Fork** this repository.
2. Create a **Branch** (`git checkout -b feature/NewFeature`).
3. Make your changes and **Commit** (`git commit -m 'Add: New feature'`).
4. **Push** your code (`git push origin feature/NewFeature`).
5. Open a **Pull Request**.

---

<a name="contact"></a>
## Contact
**Haluk Can Sarıöz**
- GitHub: [@halukcansarioz](https://github.com/halukcansarioz)
- Email: [halukcansarioz19@gmail.com](mailto:halukcansarioz19@gmail.com)
- LinkedIn: [Haluk Can Sarıöz](https://www.linkedin.com/in/halukcansarioz)

---

*If you found this computer vision project helpful, don't forget to ⭐ it!*

---

## License
This project is licensed under the [MIT License](LICENSE).
