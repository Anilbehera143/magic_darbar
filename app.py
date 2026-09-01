import streamlit as st

st.set_page_config(page_title="Magic Heart Core", page_icon="💖", layout="wide")

# Step 1: Only the Glowing Pulsing Heart Code (Pure English)
heart_step_code = """
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
            background-color: #030308;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        /* Pure CSS Glowing Pulsing Heart */
        .neon-heart {
            position: relative;
            width: 150px;
            height: 150px;
            background: linear-gradient(135deg, #ff007f, #ff3366);
            transform: rotate(-45deg);
            box-shadow: 0 0 50px #ff007f, 0 0 100px #7f00ff;
            animation: heart-pulse 1.2s infinite ease-in-out;
        }

        .neon-heart::before,
        .neon-heart::after {
            content: '';
            position: absolute;
            width: 150px;
            height: 150px;
            background: linear-gradient(135deg, #ff007f, #ff3366);
            border-radius: 50%;
        }

        .neon-heart::before {
            top: -75px;
            left: 0;
        }

        .neon-heart::after {
            left: 75px;
            top: 0;
        }

        @keyframes heart-pulse {
            0% {
                transform: rotate(-45deg) scale(0.95);
                box-shadow: 0 0 40px #ff007f, 0 0 80px #7f00ff;
            }
            50% {
                transform: rotate(-45deg) scale(1.1);
                box-shadow: 0 0 70px #ff007f, 0 0 130px #00f0ff;
            }
            100% {
                transform: rotate(-45deg) scale(0.95);
                box-shadow: 0 0 40px #ff007f, 0 0 80px #7f00ff;
            }
        }
    </style>
</head>
<body>
    <div class="neon-heart"></div>
</body>
</html>
"""

# Render the single beating heart on screen
st.components.v1.html(heart_step_code, height=500, scrolling=False)
