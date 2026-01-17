import streamlit as st
import time
import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="AETHER Web",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS (Tampilan Modern & Bersih) ---
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #00c6ff;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #1f2937;
        border: 1px solid #374151;
        margin-bottom: 15px;
    }
    .highlight {
        color: #4CAF50;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGASI (SIDEBAR) ---
with st.sidebar:
    st.title("🌌 AETHER")
    st.caption("Adaptive Neural Interface")
    
    menu = st.radio("Menu Utama", ["⚡ Smart Dashboard", "📝 Blog & Wawasan", "ℹ️ Tentang"])
    
    st.divider()
    st.write("Setel Kondisi Anda:")
    mood = st.select_slider("Bagaimana perasaan Anda saat ini?", 
                            options=["Sangat Stres", "Lelah", "Netral", "Fokus", "Bersemangat"])
    
    st.divider()
    st.caption("© 2025 AETHER Project")

# --- HALAMAN 1: SMART DASHBOARD (ALAT BANTU) ---
if menu == "⚡ Smart Dashboard":
    st.title(f"Halo, Mode: {mood}")
    
    # Logika Liquid UI: Tampilan berubah sesuai Mood
    if mood == "Sangat Stres":
        st.error("⚠️ Terdeteksi Beban Mental Tinggi")
        st.markdown("""
        <div class="card">
            <h3>💊 Resep Digital: De-Stress</h3>
            <p>Sistem mendeteksi Anda butuh ketenangan. Matikan notifikasi HP Anda sejenak.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("🌬️ Panduan Napas 4-7-8")
            if st.button("Mulai Terapi Napas"):
                with st.empty():
                    for i in range(3):
                        st.write("🛑 Tahan Napas...")
                        time.sleep(2)
                        st.write("💨 Hembuskan Perlahan...")
                        time.sleep(2)
                    st.success("Selesai. Ulangi jika perlu.")
        with col2:
            st.video("https://www.youtube.com/watch?v=lFcSrYw-ARY") # Musik relaksasi
            
    elif mood == "Fokus" or mood == "Bersemangat":
        st.success("🚀 Mode Produktivitas Tinggi Aktif")
        st.markdown("""
        <div class="card">
            <h3>🎯 Deep Work Station</h3>
            <p>Manfaatkan energi ini untuk menyelesaikan tugas tersulit Anda.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2,1])
        with col1:
            task = st.text_input("Apa 1 Tugas Utama hari ini?")
            if task:
                st.write(f"FOKUS SAJA PADA: **{task}**")
                # Pomodoro Timer Sederhana
                if st.button("Mulai Timer Fokus (25 Menit)"):
                    bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.1) # Dipercepat untuk demo
                        bar.progress(i + 1)
                    st.balloons()
                    st.write("Waktu istirahat!")
        with col2:
             st.write("🎶 **Rekomendasi Audio:** Binaural Beats (40Hz)")
             st.markdown("[Buka Spotify Focus](https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ)")

    else: # Netral / Lelah
        st.warning("🔋 Mode Hemat Energi")
        st.write("Lakukan hal-hal ringan. Rapikan meja, balas email pendek, atau baca artikel di Blog.")

# --- HALAMAN 2: BLOG (TEMPAT BERBAGI) ---
elif menu == "📝 Blog & Wawasan":
    st.title("Wawasan AETHER")
    st.write("Artikel terpilih untuk meningkatkan kualitas hidup dan teknologi.")

    # Artikel 1
    with st.expander("🤖 Masa Depan AI adalah 'Teman', Bukan Alat", expanded=True):
        st.markdown("""
        **Ditulis oleh Admin** | 25 Des 2025
        
        Banyak orang takut AI akan menggantikan manusia. Padahal, masa depan yang ideal adalah *Simbiosis*.
        AETHER dirancang bukan untuk menyuruh Anda, tapi untuk *memahami* kondisi emosi Anda sebelum Anda bekerja.
        
        Teknologi harusnya membuat kita lebih tenang, bukan lebih sibuk.
        """)

    # Artikel 2
    with st.expander("💡 Cara Mengelola Stres Digital"):
        st.write("""
        1. Matikan notifikasi yang tidak perlu (Non-Human Notifications).
        2. Gunakan mode 'Grayscale' pada layar HP.
        3. Gunakan fitur 'Smart Dashboard' di aplikasi ini saat merasa cemas.
        """)
        
    # Form Request Artikel
    st.markdown("---")
    st.write("**Punya ide topik?**")
    st.text_input("Kirim saran topik artikel di sini:")
    if st.button("Kirim Saran"):
        st.success("Terima kasih! Saran Anda tersimpan di sistem.")

# --- HALAMAN 3: TENTANG ---
elif menu == "ℹ️ Tentang":
    st.title("Tentang AETHER Project")
    st.info("Aplikasi ini dibuat untuk membantu manusia menyeimbangkan Produktivitas dan Kesehatan Mental.")
    st.write("Versi Web 1.0 - Dibuat dengan Python & Streamlit.")