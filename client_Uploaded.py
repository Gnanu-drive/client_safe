import streamlit as st

st.set_page_config(layout="centered")
st.title("📤 Camera Streamer")

# Set this to your laptop's local IP on same Wi-Fi (e.g., 192.168.x.x)
upload_url = "https://cce2-2409-40f2-146-74ea-d415-9c4f-b372-154c.ngrok-free.app/upload"  # <-- Replace with actual IP

st.markdown(f"""
This app streams camera frames to:

`POST {upload_url}`

Make sure your laptop is running the Flask app and both devices are on the same Wi-Fi.
""")

st.components.v1.html(f"""
<video id="video" autoplay playsinline width="100%" style="max-width: 400px;"></video>
<canvas id="canvas" style="display:none;"></canvas>

<script>
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const uploadUrl = "{upload_url}";

navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: "user" }} }})
  .then(stream => {{
    video.srcObject = stream;
  }})
  .catch(err => {{
    alert("Webcam access denied: " + err);
  }});

setInterval(() => {{
  if (video.readyState === video.HAVE_ENOUGH_DATA) {{
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);
    canvas.toBlob(blob => {{
      const formData = new FormData();
      formData.append('frame', blob, 'frame.jpg');
      fetch(uploadUrl, {{
        method: 'POST',
        body: formData
      }}).catch(e => console.log("Upload error", e));
    }}, 'image/jpeg');
  }}
}}, 1000);  // 1 frame per second
</script>
""", height=480)
