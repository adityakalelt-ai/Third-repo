# Real-Time Face Detection System

**Author:** Aditya Kale  
**College:** Y.C.C.E  
**GitHub:** [@adityakalelt-ai](https://github.com/adityakalelt-ai)  
**Repository:** [third-repo](https://github.com/adityakalelt-ai/third-repo)

---

## Project Overview

This is my Machine Learning / Computer Vision project built using Python and OpenCV.  
The application uses a webcam to detect human faces in real time, draws green boxes around them, and shows a live face count on the screen.

I built the project structure, Python setup, virtual environment, main logic, face counter, and debugging myself. For OpenCV functions like `VideoCapture`, `CascadeClassifier`, and `detectMultiScale`, I referred to the official OpenCV documentation.

---

## Features

- Live webcam face detection
- Green bounding boxes around detected faces
- Real-time face counter (`Faces: X`)
- Uses pre-trained Haar Cascade model (no training needed)
- Clean folder structure with virtual environment

---

## Technologies Used

| Tool | Use |
|------|-----|
| Python 3.14 | Main programming language |
| OpenCV | Webcam, face detection, display window |
| NumPy | Image data handling |
| Haar Cascade XML | Pre-trained face detection model |

---

## Project Structure

```
ml project/
├── src/
│   └── face_detector.py
├── models/
│   └── haarcascade_frontalface_default.xml
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

**Note:** The `venv/` folder is created locally on each machine. It is not uploaded to GitHub.

---

## How It Works

1. Webcam sends live video frames to Python
2. Each frame is converted to grayscale
3. Haar Cascade model detects faces in the frame
4. Green rectangles are drawn around faces
5. Face count is shown on the screen
6. Press `q` on the video window to exit

---

## Setup Instructions

### Requirements
- Python 3.10 or higher
- Webcam
- Windows / macOS / Linux

### Step 1: Download the project
Download or clone this repository from GitHub.

### Step 2: Create virtual environment
```bash
python -m venv venv
```

### Step 3: Activate virtual environment

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install packages
```bash
pip install -r requirements.txt
```

### Step 5: Run the project
```bash
python src/face_detector.py
```

### Step 6: Use the application
- A window named **Real-Time Face Detection** will open
- Show your face to the camera
- Green boxes and face count will appear
- Click the video window and press **`q`** to quit

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Python not found | Install Python and enable "Add to PATH" |
| Webcam not opening | Close Zoom/Teams and check camera privacy settings |
| Failed to read frame (Windows) | Code already uses `cv2.CAP_DSHOW` for Windows |
| `q` not working | Click the video window first, then press `q` |
| NumPy install error | Use updated versions in `requirements.txt` |

---

## What I Learned

- Python project folder structure
- Virtual environment and `requirements.txt`
- Real-time video processing with OpenCV
- Haar Cascade based face detection
- Drawing text and shapes on video frames
- Debugging webcam and package issues on Windows

---

## References

- [OpenCV Documentation](https://docs.opencv.org/)
- [OpenCV Haar Cascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
