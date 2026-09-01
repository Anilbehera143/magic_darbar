import streamlit as st

st.set_page_config(page_title="MAYA OS v7.0 - Neural Interface", page_icon="⚡", layout="wide")

# Full HTML/CSS Futuristic MAYA OS Dashboard Code (Pure English)
maya_dashboard_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            background-color: #02050e;
            color: #00f0ff;
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            padding: 10px;
            overflow: hidden;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #00f0ff55;
            padding-bottom: 5px;
            font-size: 14px;
        }
        .main-grid {
            display: grid;
            grid-template-columns: 250px 1fr 250px;
            gap: 15px;
            margin-top: 15px;
            height: 80vh;
        }
        .panel {
            background: rgba(0, 240, 255, 0.03);
            border: 1px solid #00f0ff44;
            border-radius: 6px;
            padding: 10px;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.1);
        }
        .panel-title {
            font-size: 12px;
            color: #ff007f;
            border-bottom: 1px dashed #ff007f55;
            margin-bottom: 8px;
            padding-bottom: 3px;
        }
        .center-core {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
        }
        .holo-sphere {
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: conic-gradient(from 0deg at 50% 50%, #ff007f, #7f00ff, #00f0ff, #00ff7f, #ff007f);
            box-shadow: 0 0 50px #00f0ff, inset 0 0 30px #ffffff;
            animation: spin 6s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .stat-bar {
            background: #00f0ff22;
            height: 8px;
            border-radius: 4px;
            margin-top: 5px;
            overflow: hidden;
        }
        .stat-fill {
            background: #00f0ff;
            height: 100%;
            width: 65%;
        }
    </style>
</head>
<body>
    <div class="header">
        <div><b>MAYA OS v7.0</b> // NEURAL INTERFACE</div>
        <div id="clock">19:53:48</div>
        <div>SYSTEM STATUS: <span style="color:#00ffcc;">ONLINE</span></div>
    </div>

    <div class="main-grid">
        <div class="panel">
            <div class="panel-title">SYSTEM METRICS</div>
            <p style="font-size:11px; margin:5px 0;">CORE LOAD</p>
            <div class="stat-bar"><div class="stat-fill" style="width: 78%;"></div></div>
            <p style="font-size:11px; margin:10px 0 5px 0;">NEURAL SYNC</p>
            <div class="stat-bar"><div class="stat-fill" style="width: 92%; background:#ff007f;"></div></div>
            <p style="font-size:11px; margin:10px 0 5px 0;">MEMORY BUFFER</p>
            <div class="stat-bar"><div class="stat-fill" style="width: 45%; background:#00ffcc;"></div></div>
        </div>

        <div class="panel center-core">
            <div class="holo-sphere"></div>
            <h3 style="margin-top: 15px; letter-spacing: 2px; color: #00f0ff;">ADVANCED NEURAL CORE</h3>
            <p style="font-size: 11px; color: #a78bfa;">POWERED BY MAYA AI v7.0</p>
        </div>

        <div class="panel">
            <div class="panel-title">CORE MODULES</div>
            <ul style="font-size: 11px; padding-left: 15px; line-height: 1.8; color: #a78bfa;">
                <li>NEURAL ENGINE</li>
                <li>VOICE SYNTHESIS</li>
                <li>VISION SUBSYSTEM</li>
                <li>QUANTUM CORE</li>
                <li>ADAPTIVE AI MODEL</li>
            </ul>
        </div>
    </div>

    <script>
        setInterval(() => {
            const d = new Date();
            document.getElementById('clock').innerText = d.toTimeString().split(' ')[0];
        }, 1000);
    </script>
</body>
</html>
"""

# Render the HTML dashboard inside Streamlit with proper height
st.components.v1.html(maya_dashboard_code, height=580, scrolling=False)

# Terminal Input Section at bottom
st.markdown("---")
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "MAYA OS terminal initialized, Anil. All core modules are active."}
    ]

for msg in st.session_state.messages:
    avatar = "⚡" if msg["role"] == "assistant" else "💻"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

if prompt := st.chat_input("Enter command into MAYA OS terminal..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="💻"):
        st.markdown(prompt)

    response = f"Command successfully parsed: '{prompt}'. Executing core instructions, Anil."
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar="⚡"):
        st.markdown(response)
import streamlit as st

st.set_page_config(page_title="MAYA OS v7.0", page_icon="⚡", layout="wide")

# Full Screen Responsive MAYA OS Code (Pure English)
maya_fullscreen_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        * { box-sizing: border-box; }
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100vh;
            background-color: #02050e;
            color: #00f0ff;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
        }
        .main-wrapper {
            display: flex;
            flex-direction: column;
            height: 100vh;
            padding: 15px;
        }
        .top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid rgba(0, 240, 255, 0.4);
            padding-bottom: 10px;
            font-size: 16px;
            letter-spacing: 1px;
        }
        .dashboard-grid {
            display: grid;
            grid-template-columns: 280px 1fr 280px;
            gap: 20px;
            flex-grow: 1;
            margin-top: 15px;
        }
        .side-box, .center-box {
            background: rgba(0, 240, 255, 0.02);
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.08);
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .box-title {
            font-size: 13px;
            color: #ff007f;
            border-bottom: 1px dashed rgba(255, 0, 127, 0.4);
            margin-bottom: 12px;
            padding-bottom: 5px;
            font-weight: bold;
        }
        .center-box {
            align-items: center;
            text-align: center;
        }
        .holo-orb {
            width: 250px;
            height: 250px;
            border-radius: 50%;
            background: conic-gradient(from 0deg at 50% 50%, #ff007f, #7f00ff, #00f0ff, #00ff7f, #ff007f);
            box-shadow: 0 0 60px #00f0ff, inset 0 0 40px #ffffff;
            animation: spin-orb 6s linear infinite;
        }
        @keyframes spin-orb {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .metric-bar {
            background: rgba(0, 240, 255, 0.1);
            height: 10px;
            border-radius: 5px;
            margin-top: 6px;
            margin-bottom: 15px;
            overflow: hidden;
        }
        .metric-fill {
            background: #00f0ff;
            height: 100%;
            width: 75%;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="top-header">
            <div><b>MAYA OS v7.0</b> // SYSTEM INTERFACE</div>
            <div id="live-clock">00:00:00</div>
            <div>STATUS: <span style="color:#00ffcc;">ONLINE & SECURE</span></div>
        </div>

        <div class="dashboard-grid">
            <div class="side-box">
                <div class="box-title">SYSTEM METRICS</div>
                <p style="font-size: 12px; margin: 0;">CORE PROCESSOR LOAD</p>
                <div class="metric-bar"><div class="metric-fill" style="width: 82%;"></div></div>
                
                <p style="font-size: 12px; margin: 0;">NEURAL NETWORK SYNC</p>
                <div class="metric-bar"><div class="metric-fill" style="width: 95%; background: #ff007f;"></div></div>
                
                <p style="font-size: 12px; margin: 0;">QUANTUM MEMORY</p>
                <div class="metric-bar"><div class="metric-fill" style="width: 58%; background: #00ffcc;"></div></div>
            </div>

            <div class="center-box">
                <div class="holo-orb"></div>
                <h2 style="margin-top: 20px; letter-spacing: 3px; color: #00f0ff; font-size: 22px;">ADVANCED NEURAL CORE</h2>
                <p style="font-size: 13px; color: #a78bfa; margin-top: 5px;">ALL SUBSYSTEMS FULLY OPERATIONAL</p>
            </div>

            <div class="side-box">
                <div class="box-title">ACTIVE MODULES</div>
                <ul style="font-size: 12px; padding-left: 18px; line-height: 2; color: #a78bfa;">
                    <li>NEURAL VOICE ENGINE</li>
                    <li>QUANTUM DATA PROCESSOR</li>
                    <li>HOLOGRAPHIC RENDERER</li>
                    <li>SECURITY PROTOCOL v7</li>
                    <li>AUTONOMOUS AI CORE</li>
                </ul>
            </div>
        </div>
    </div>

    <script>
        setInterval(() => {
            const d = new Date();
            document.getElementById('live-clock').innerText = d.toTimeString().split(' ')[0];
        }, 1000);
    </script>
</body>
</html>
"""

# Render full screen component with proper height
st.components.v1.html(maya_fullscreen_code, height=650, scrolling=False)
