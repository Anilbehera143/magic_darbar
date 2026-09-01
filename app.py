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
