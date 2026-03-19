# 🖼️  Computer vision with YOLOv8 (Real-Time Object Detection App)

A real-time object detection web application built using YOLOv8, Streamlit, and WebRTC.  
This app allows users to perform live object detection directly from their browser using their webcam, no local setup required.

This project demonstrates how a Computer vision model can be deployed interactively through an intuitive Streamlit web interface.

---

## 🚀 Features

- 🎥 Live video feed directly in the browser using webcam
- 🧠 Fast detection using YOLOv8 model
- ⚡ Streamlit caching for faster performance (avoids model reloads) 
- 🖼️ Bounding boxes and labels displayed in real time
- 🔒 No video or images are stored, all processing happens in memory
- ⚡ The audio output has been disabled for better experience

---


## 🧠 Model Overview

This application uses the YOLOv8 (You Only Look Once version 8) model from Ultralytics for real-time object detection.  
YOLOv8 is a state-of-the-art deep learning model designed for fast and accurate object detection. It processes an entire image in a single pass, making it highly efficient for real-time applications such as video streaming.

---

## 📦 Dependencies

The app uses the following Python libraries:
```
streamlit==1.55.0 
streamlit-webrtc==0.64.5
opencv-python==4.12.0.88
ultralytics==8.3.240
```
Install them using:

```bash
pip install -r requirements.txt
```
---

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run object_detection_YOLOv8.py
```
Once running, open the local address shown in the terminal (usually):

```bash
http://localhost:8501
```
Run the app directly on your edge device without downloading the code. 
```bash
https://srijan-computervisionwithyolov8.streamlit.app/
```
---

## 🌐 Deployment

This app is hosted on Streamlit Cloud, accessible directly from the browser, no installation required.

---

## 🔮 Possible Future Improvements

- Object tracking (e.g., DeepSORT / ByteTrack)
- Custom YOLO model support
- FPS counter and performance metrics
- Detection filtering (e.g., detect only people)
- Deployment on Streamlit Cloud

---
## 🛠 Tech Stack

- Python
- Streamlit
- streamlit-webrtc
- OpenCV
- Ultralytics YOLOv8
 
---

## ⚠️ Disclaimer
This project uses a pretrained model for educational and demonstration purposes.
Predictions may not always be accurate and should not be used for high-stakes or production-critical applications.

---

## 👤 Creator
SRIJAN KUMAR SAHA

---

## 📜 License

This project is intended for educational and research purposes.
