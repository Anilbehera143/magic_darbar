import streamlit as st

st.set_page_config(page_title="Cybernetic Hand Core", page_icon="⚡", layout="wide")

# Step 3: High-Tech Digital Robotic Hand with Glowing Neural Lines (Pure English)
tech_hand_code = """
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

        .container {
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        /* Holographic Glowing Palm / Hand Graphic using futuristic CSS */
        .cyber-hand {
            position: relative;
            width: 180px;
            height: 220px;
            background: radial-gradient(circle, rgba(0,240,255,0.2) 0%, rgba(2,5,14,0.9) 80%);
            border: 2px solid rgba(0, 240, 255, 0.5);
            border-radius: 40px 40px 60px 60px;
            box-shadow: 0 0 50px rgba(0, 240, 255, 0.4), inset 0 0 30px rgba(0, 240, 255, 0.3);
            display: flex;
            justify-content: center;
            align-items: center;
            animation: hand-pulse 2s ease-in-out infinite alternate;
        }

        /* Glowing Palm Lines (Hand Lines / Neural Paths) */
        .palm-line-1 {
            position: absolute;
            width: 80px;
            height: 3px;
            background: #ff007f;
            box-shadow: 0 0 10px #ff007f;
            transform: rotate(45deg);
            top: 90px;
            left: 50px;
            animation: line-glow 1.5s infinite alternate;
        }

        .palm-line-2 {
            position: absolute;
            width: 70px;
            height: 3px;
            background: #00f0ff;
            box-shadow: 0 0 10px #00f0ff;
            transform: rotate(-35deg);
            top: 110px;
            left: 55px;
            animation: line-glow 1s infinite alternate;
        }

        .palm-line-3 {
            position: absolute;
            width: 50px;
            height: 3px;
            background: #00ffcc;
            box-shadow: 0 0 10px #00ffcc;
            transform: rotate(90deg);
            top: 130px;
            left: 65px;
            animation: line-glow 2s infinite alternate;
        }

        /* Rotating Energy Rings Around Hand */
        .energy-ring {
            position: absolute;
            width: 280px;
            height: 280px;
            border-radius: 50%;
            border: 2px dashed rgba(255, 0, 127, 0.4);
            animation: spin 12s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes hand-pulse {
            0% { box-shadow: 0 0 30px rgba(0, 240, 255, 0.3); transform: scale(0.98); }
            100% { box-shadow: 0 0 70px rgba(0, 240, 255, 0.7); transform: scale(1.03); }
        }

        @keyframes line-glow {
            0% { opacity: 0.4; }
            100% { opacity: 1; filter: drop-shadow(0 0 8px #ffffff); }
        }

        .status-text {
            margin-top: 30px;
            color: #00f0ff;
            font-size: 14px;
            letter-spacing: 3px;
            text-shadow: 0 0 10px rgba(0, 240, 255, 0.8);
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="energy-ring"></div>
        <div class="cyber-hand">
            <div class="palm-line-1"></div>
            <div class="palm-line-2"></div>
            <div class="palm-line-
File "/mount/src/magic_darbar/app.py", line 6
  tech_hand_code = """
                   ^
SyntaxError: unterminated triple-quoted string literal (detected at line 126)
File "/mount/src/magic_darbar/app.py", line 129
                     ^
                    ^
IndentationError: unexpected indent
