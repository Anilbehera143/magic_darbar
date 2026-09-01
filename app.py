import streamlit as st

st.set_page_config(page_title="Advanced Holographic War-Room", page_icon="🌐", layout="wide")

# Advanced 3D Blue Holographic War-Room Interface (Pure English & Ultra-Realistic)
holo_warroom_code = """
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
            background-color: #000208;
            color: #00f0ff;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Hologram Container */
        .holo-space {
            position: relative;
            width: 500px;
            height: 500px;
            display: flex;
            justify-content: center;
            align-items: center;
            perspective: 1000px;
        }

        /* Outer Military Grid Ring */
        .grid-ring-outer {
            position: absolute;
            width: 440px;
            height: 440px;
            border-radius: 50%;
            border: 1px dashed rgba(0, 240, 255, 0.3);
            border-top: 3px solid #00f0ff;
            border-bottom: 3px solid #00f0ff;
            animation: spin-cw 20s linear infinite;
        }

        /* Middle Rotating Radar Ring */
        .grid-ring-middle {
            position: absolute;
            width: 350px;
            height: 350px;
            border-radius: 50%;
            border: 2px solid rgba(0, 150, 255, 0.4);
            border-left: 3px solid #ff007f;
            border-right: 3px solid #ff007f;
            animation: spin-ccw 12s linear infinite;
        }

        /* Inner Quantum Scanner Ring */
        .grid-ring-inner {
            position: absolute;
            width: 260px;
            height: 260px;
            border-radius: 50%;
            border: 1px solid rgba(0, 255, 204, 0.6);
            box-shadow: inset 0 0 30px rgba(0, 240, 255, 0.3), 0 0 30px rgba(0, 240, 255, 0.2);
            animation: spin-cw 8s linear infinite;
        }

        /* Center Holographic Core / Blue Star */
        .holo-core {
            position: absolute;
            width: 130px;
            height: 130px;
            border-radius: 50%;
            background: radial-gradient(circle, #ffffff 0%, #00f0ff 40%, #002244 80%, transparent 100%);
            box-shadow: 0 0 60px #00f0ff, 0 0 120px rgba(0, 240, 255, 0.8);
            animation: core-pulse 3s ease-in-out infinite alternate;
        }

        @keyframes spin-cw {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes spin-ccw {
            0% { transform: rotate(360deg); }
            100% { transform: rotate(0deg); }
        }

        @keyframes core-pulse {
            0% { transform: scale(0.92); opacity: 0.8; box-shadow: 0 0 40px #00f0ff; }
            100% { transform: scale(1.08); opacity: 1; box-shadow: 0 0 90px #00f0ff, 0 0 150px rgba(0,240,255,0.9); }
        }

        .hud-status {
            position: absolute;
            bottom: -80px;
            font-size: 13px;
            letter-spacing: 5px;
            color: #00f0ff;
            text-shadow: 0 0 15px rgba(0, 240, 255, 0.9);
            text-align: center;
            text-transform: uppercase;
        }
    </style>
</head>
<body>
    <div class="holo-space">
        <div class="grid-ring-outer"></div>
        <div class="grid-ring-middle"></div>
        <div class="grid-ring-inner"></div>
        <div class="holo-core"></div>
        <div class="hud-status">HOLOGRAPHIC QUANTUM MATRIX // SECURE</div>
    </div>
</body>
</html>
"""

# Render the High-Tech Hologram in Streamlit
st.components.v1.html(holo_warroom_code, height=580, scrolling=False)
