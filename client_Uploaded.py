import streamlit as st
import cv2
import time
import requests
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

# Configuration
UPLOAD_URL = "https://66fb-2409-40f2-146-74ea-7057-78f-2c52-9437.ngrok-free.app/upload"

st.set_page_config(page_title="📤 Camera Stream to Server", layout="centered")
st.title("📱 Stream Camera to Remote Server")

st.markdown(
    """
This app will access your webcam and **stream frames** to a remote server endpoint.

✅ Ensure camera permission is granted.  
📡 Target: `POST {UPLOAD_URL}`  
"""
)

# --- Video Processor to POST each frame ---
class FrameSender(VideoTransformerBase):
    def __init__(self):
        self.last_post_time = 0
        self.post_interval = 1  # seconds

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Throttle sending to once per second
        if time.time() - self.last_post_time > self.post_interval:
            _, buffer = cv2.imencode('.jpg', img)
            try:
                requests.post(UPLOAD_URL, files={"frame": buffer.tobytes()}, timeout=1)
            except Exception as e:
                print("Failed to send frame:", e)
            self.last_post_time = time.time()

        return av.VideoFrame.from_ndarray(img, format="bgr24")

# Start the camera stream
webrtc_streamer(
    key="camera-sender",
    video_transformer_factory=FrameSender,
    media_stream_constraints={"video": {"facingMode": "user"}, "audio": False},
    sendback_audio=False,
)
