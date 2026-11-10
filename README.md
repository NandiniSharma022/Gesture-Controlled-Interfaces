# 🖐️ Gesture-Controlled Interface

A real-time hand gesture recognition system that enables touchless computer interaction using Python and Computer Vision.

## 📌 About the Project

Gesture-Controlled Interface is a Python-based application that uses a webcam to detect and track hand movements. It translates specific hand gestures into computer actions, allowing users to control the mouse cursor without physically touching a mouse.

## ✨ Features

- Real-time hand tracking using MediaPipe.
- Hand landmark detection.
- Gesture-based mouse cursor movement.
- Pinch gesture detection for clicking.
- Touchless computer interaction.
- Real-time webcam processing.

## 🛠️ Tech Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Core programming     |
| OpenCV     | Image processing     |
| MediaPipe  | Hand tracking        |
| PyAutoGUI  | Mouse control        |
| NumPy      | Numerical operations |

## 📂 Project Structure

```text
Gesture-Controlled-Interfaces/
├── gesture-main.py
├── gesture_logic.py
├── README.md
├── requirements.txt
├── .gitignore
└── assets/
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/NandiniSharma022/Gesture-Controlled-Interfaces.git
```

**2. Navigate to the project**

```bash
cd Gesture-Controlled-Interfaces
```

**3. Create a virtual environment**

```bash
python3 -m venv .venv
```

**4. Activate the environment**

```bash
source .venv/bin/activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
python gesture-main.py
```

## 🧠 How It Works

1. Webcam captures live video.
2. MediaPipe detects hand landmarks.
3. Gesture logic interprets finger positions.
4. PyAutoGUI converts recognized gestures into mouse actions.

## 📸 Screenshots & Demo

Screenshots and demonstration videos will be added here.

## 🔮 Future Improvements

- Add more customizable hand gestures.
- Introduce keyboard shortcuts through gestures.
- Improve gesture recognition accuracy.
- Add a graphical user interface (GUI).

## 👩‍💻 Author

**Nandini Sharma**

GitHub: [NandiniSharma022](https://github.com/NandiniSharma022)

---

⭐ If you find this project interesting, consider giving it a star!
