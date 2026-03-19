from ultralytics import YOLO
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase 

@st.cache_resource
def load_model():
    model = YOLO("yolov8n.pt")
    return model

model= load_model()
st.header("Object Classifier with YOLOv8n", divider="rainbow")

st.sidebar.markdown("#### Project by SRIJAN KUMAR SAHA")

st.markdown("A object detection web application powered by a state-of-the-art real-time object detection model YOLOv8, which enables users to perform live object detection directly through their edge devices.")

st.markdown("##### Project Features:\n"
    "- Real-Time Object Classification, powered by YOLOv8n.\n"
    "- All processing happens in real time without storing images, video, or personal data..\n"
    "- Clear bounding boxes and labels displayed in real time for easy interpretation of detected objects.\n"
    "- Optimized for smooth streaming with minimal latency.\n"
    "- Uses Streamlit caching to avoid reloading the model multiple times for faster performance.\n")

st. markdown("##### Note: When running this app on a device with multiple cameras available, one can switch between the camera inputs from the 'SELECT DEVICE' option")

class YOLOProcessor(VideoTransformerBase):
    
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        #flip the image
        #img =cv2.flip(img,1) # 1: rotates the image horizontally, 0: vertically, -1: both horizontally and vertically

        # Run YOLO detection
        results = model(img, show= False)

        # Draw results
        annotated_frame = results[0].plot()

        return annotated_frame

webrtc_streamer(
    key="yolo",
    video_processor_factory=YOLOProcessor,
    sendback_audio = False
)


