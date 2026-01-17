import streamlit as st
import time
import random

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="AETHER CORE",
    page_icon="🌌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS STYLING (BIAR SENADA SAMA WEB OM KOLONG) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0f0c29;
        color: #e0f7fa;
    }
    h1, h2, h3 {
        color: #00e6e6 !important;
        text-shadow: 0 0 10px #00e6e6;
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00e6e6, #007bff);
        color: white;
        border: none;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,230,230,0.5);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0,230,230,0.8);
    }
    .big-font {
        font-size: 60px !important;
        font-weight: bold;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 20px #ff00ff;
    }
    .glass-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(0, 230, 230, 0.3);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>🌌 AETHER CORE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.7;'>System Activated. Choose your module.</p>", unsafe_allow_html=True)

# --- TAB NAVIGASI ---
tab1, tab2, tab3 = st.tabs(["⏱️ Deep Focus", "🫁 Zen Breath", "🤖 Oracle AI"])

# === FITUR 1: DEEP FOCUS (POMODORO) ===
with tab1:
    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
    st.subheader("Deep Focus Timer")
    st.write("Atur waktu fokus lo biar produktif, Bro.")
    
    col1, col2 = st.columns(2)
    with col1:
        minutes = st.number_input("Menit:", min_value=1, max_value=120, value=25)
    with col2:
        st.write("") # Spacer
        st.write("")
        start_focus = st.button("Mulai Fokus 🔥")

    if start_focus:
        with st.empty():
            total_seconds = minutes * 60
            while total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)
                timer_display = '{:02d}:{:02d}'.format(mins, secs)
                st.markdown(f"<p class='big-font'>{timer_display}</p>", unsafe_allow_html=True)
                time.sleep(1)
                total_seconds -= 1
            st.markdown("<p class='big-font'>SELESAI! 🚀</p>", unsafe_allow_html=True)
            st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)

# === FITUR 2: ZEN BREATHING ===
with tab2:
    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
    st.subheader("Zen Breathing")
    st.write("Ikuti panduan ini kalau lo lagi stres atau panik.")
    
    if st.button("Mulai Terapi Napas 🌬️"):
        progress_text = "Siap-siap..."
        my_bar = st.progress(0, text=progress_text)
        status_text = st.empty()

        for cycle in range(3): # 3 Siklus
            # Tarik Napas (4 detik)
            status_text.markdown("## 🔼 TARIK NAPAS...")
            for i in range(100):
                time.sleep(0.04)
                my_bar.progress(i + 1)
            
            # Tahan (4 detik)
            status_text.markdown("## ⏸️ TAHAN...")
            time.sleep(4)
            
            # Hembuskan (4 detik)
            status_text.markdown("## 🔽 HEMBUSKAN...")
            for i in range(100, 0, -1):
                time.sleep(0.04)
                my_bar.progress(i)
        
        status_text.markdown("## ✨ Rileks...")
        st.success("Sesi selesai. Semoga lebih tenang!")
    st.markdown("</div>", unsafe_allow_html=True)

# === FITUR 3: AETHER ORACLE ===
with tab3:
    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
    st.subheader("Aether Oracle")
    st.write("Tanya apa aja, AI akan kasih petunjuk random.")
    
    question = st.text_input("Ketik pertanyaan lo (Ya/Tidak):", placeholder="Misal: Apakah dia jodoh gw?")
    
    if st.button("Tanya Oracle 🔮") and question:
        with st.spinner("Menghubungkan ke dimensi lain..."):
            time.sleep(2) # Efek mikir
            answers = [
                "Pasti banget, Bro!", 
                "Kayaknya nggak dulu deh.", 
                "Coba tanya lagi besok.",
                "Energinya positif, GAS!",
                "Hati-hati, ada red flag.",
                "Fokus karir dulu aja.",
                "100% Valid!",
                "Mending tidur aja."
            ]
            result = random.choice(answers)
            st.markdown(f"<h2 style='text-align:center; color:#ff00ff;'>{result}</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.caption("Powered by Streamlit | Om Kolong Techno Engine V2.0")
