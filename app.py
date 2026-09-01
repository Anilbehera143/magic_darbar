import streamlit as st

st.set_page_config(page_title="Cybernetic Tech Heart", page_icon="⚡", layout="wide")

# Step 2: High-Tech Cybernetic Holographic Heart (Pure English)
tech_heart_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100vh;
            background-color: #02050e;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            font-family: 'Courier New', Courier, monospace;
        }

        /* Container for Tech Core */
        .tech-container {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Rotating Tech Rings Around the Heart */
        .tech-ring {
            position: absolute;
            width: 260px;
            height: 260px;
            border-radius: 50%;
            border: 2px dashed rgba(0, 240, 255, 0.4);
            animation: spin-ring 10s linear infinite;
        }

        .tech-ring-2 {
            position: absolute;
            width: 320px;
            height: 320px;
            border-radius: 50%;
            border: 1px solid rgba(255, 0, 127, 0.3);
            animation: spin-ring-rev 15s linear infinite;
        }

        /* Futuristic Neon Tech Heart */
        .cyber-heart {
            position: relative;
            width: 140px;
            height: 140px;
            background: linear-gradient(135deg, #00f0ff, #7f00ff, #ff007f);
            transform: rotate(-45deg);
            box-shadow: 0 0 40px #00f0ff, 0 0 80px #7f00ff;
            animation: tech-pulse 1s infinite ease-in-out;
        }

        .cyber-heart::before,
        .cyber-heart::after {
            content: '';
            position: absolute;
            width: 140px;
            height: 140px;
            background: linear-gradient(135deg, #00f0ff, #7f00ff, #ff007f);
            border-radius: 50%;
        }

        .cyber-heart::before {
            top: -70px;
            left: 0;
        }

        .cyber-heart::after {
            left: 70px;
            top: 0;
        }

        @keyframes tech-pulse {
            0% {
                transform: rotate(-45deg) scale(0.96);
                box-shadow: 0 0 30px #00f0ff, 0 0 70px #ff007f;
            }
            50% {
                transform: rotate(-45deg) scale(1.08);
                box-shadow: 0 0 60px #00f0ff, 0 0 120px #00ffcc;
            }
            100% {
                transform: rotate(-45deg) scale(0.96);
                box-shadow: 0 0 30px #00f0ff, 0 0 70px #ff007f;
            }
        }

        @keyframes spin-ring {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes spin-ring-rev {
            0% { transform: rotate(360deg); }
            100% { transform: rotate(0deg); }
        }

        .label-text {
            position: absolute;
            bottom: -80px;
            color: #00f0ff;
            font-size: 14px;
            letter-spacing: 3px;
            text-shadow: 0 0 10px rgba(0, 240, 255, 0.8);
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="tech-container">
        <div class="tech-ring-2"></div>
        <div class="tech-ring"></div>
        <div class="cyber-heart"></div>
        <div class="label-text">CYBER-CORE // ONLINE</div>
    </div>
</body>
</html>
"""

# Render the High-Tech Cyber Heart component
st.components.v1.html(tech_heart_code, height=520, scrolling=False)
