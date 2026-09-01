import streamlit as st

st.set_page_config(page_title="JARVIS // Stark Industries", page_icon="⚡", layout="wide")

# MCU JARVIS Style Futuristic Holographic Interface (Pure English)
jarvis_code = """
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
            background-color: #010409;
            color: #00f0ff;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .jarvis-container {
            position: relative;
            width: 400px;
            height: 400px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Stark Arc Reactor / Hologram Outer Ring 1 */
        .ring-outer {
            position: absolute;
            width: 360px;
            height: 360px;
            border-radius: 50%;
            border: 2px dashed rgba(0, 240, 255, 0.4);
            border-top: 2px solid #00f0ff;
            border-bottom: 2px solid #ff007f;
            animation: spin-clockwise 10s linear infinite;
        }

        /* Stark Hologram Middle Ring 2 */
        .ring-middle {
            position: absolute;
            width: 290px;
            height: 290px;
            border-radius: 50%;
            border: 3px dotted rgba(0, 255, 204, 0.5);
            animation: spin-counter 14s linear infinite;
        }

        /* Stark Hologram Inner Ring 3 */
        .ring-inner {
            position: absolute;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            border: 2px solid rgba(0, 240, 255, 0.7);
            box-shadow: 0 0 25px rgba(0, 240, 255, 0.3);
            animation: spin-clockwise 6s linear infinite;
        }

        /* Center Arc Reactor Core */
        .arc-core {
            position: absolute;
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: radial-gradient(circle, #ffffff 0%, #00f0ff 50%, #03040f 90%);
            box-shadow: 0 0 50px #00f0ff, 0 0 100px rgba(0, 240, 255, 0.8), inset 0 0 20px #ffffff;
            animation: core-glow 2s ease-in-out infinite alternate;
        }

        @keyframes spin-clockwise {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes spin-counter {
            0% { transform: rotate(360deg); }
            100% { transform: rotate(0deg); }
        }

        @keyframes core-glow {
            0% { transform: scale(0.95); box-shadow: 0 0 40px #00f0ff; }
            100% { transform: scale(1.05); box-shadow: 0 0 90px #00f0ff, 0 0 140px #ff007f; }
        }

        .hud-text {
            position: absolute;
            bottom: -70px;
            font-size: 14px;
            letter-spacing: 4px;
            color: #00f0ff;
            text-shadow: 0 0 12px rgba(0, 240, 255, 0.9);
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="jarvis-container">
        <div class="ring-outer"></div>
        <div class="ring-middle"></div>
        <div class="ring-inner"></div>
        <div class="arc-core"></div>
        <div class="hud-text">JARVIS // STARK INDUSTRIES v4.2</div>
    </div>
</body>
</html>
"""

# Render the realistic Jarvis HUD component
st.components.v1.html(jarvis_code, height=550, scrolling=False)
