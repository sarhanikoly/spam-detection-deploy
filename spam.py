import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="SPAM Detector by Desvita", page_icon="💌", layout="centered")

# Sidebar Style
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #e6e6fa 0%, #f8f8ff 100%);
    }
    .css-1d391kg {
        background-color: #f4f6f8;
    }
    </style>
""", unsafe_allow_html=True)

# Main Style
st.markdown("""
    <style>
    .stTextArea textarea {
        background-color: #fdfdfd;
        border-radius: 12px;
        font-size: 16px;
        padding: 12px;
    }
    .stButton>button {
        background-color: #8a2be2;
        color: white;
        font-weight: bold;
        padding: 10px 24px;
        border: none;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #6f1fb7;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
menu = st.sidebar.radio("📌 Navigasi", ["📨 Deteksi SPAM", "📚 Tentang Spam", "👩‍🎓 Tentang Saya"])

# Halaman: Deteksi SPAM
if menu == "📨 Deteksi SPAM":
    st.title("📨 Deteksi Pesan SPAM")
    st.markdown("Masukkan pesan kamu, dan aplikasi ini akan mendeteksi apakah itu SPAM atau bukan ✨")

    message = st.text_area("💬 Tulis pesan di sini:")

    if st.button("🚀 Deteksi Sekarang"):
        if message.strip() == "":
            st.warning("⚠️ Eh... Pesannya masih kosong sayang~")
        else:
            vect = vectorizer.transform([message]).toarray()
            result = model.predict(vect)

            if result[0] == 1:
                st.error("❌ SPAM! Jangan ditanggapi ya 😠")
            else:
                st.success("✅ Bukan SPAM. Aman digunakan 😇")

# Halaman: Tentang Spam
elif menu == "📚 Tentang Spam":
    st.title("📚 Apa Itu SPAM?")
    st.markdown("""
    **SPAM** adalah pesan yang tidak diminta, sering bersifat mengganggu, dan dikirim ke banyak orang secara massal.
    
    ### 🚨 Ciri-ciri Pesan SPAM:
    - Terlalu bagus untuk jadi kenyataan (misalnya menang hadiah)
    - Minta klik link mencurigakan
    - Meminta data pribadi atau OTP
    - Mengandung tekanan atau ancaman
    
    💡 Tips menghindari SPAM:
    - Jangan klik link sembarangan
    - Jangan balas pesan mencurigakan
    - Gunakan deteksi SPAM seperti aplikasi ini 😎
    """)

# Halaman: Tentang Saya
elif menu == "👩‍🎓 Tentang Saya":
    st.title("👩‍🎓 Desvita Sarhani Koly")
    st.markdown("""
    Hai! Aku Desvita — mahasiswi semester 4 Teknik Informatika di Universitas Nusa Putra 🏫  
    Ini adalah aplikasi sederhana hasil belajarku tentang machine learning dan Streamlit 💻

    - 📍 Asal: Maluku Tengah  
    - 💬 Hobi: Masak, belajar teknologi, dan bikin pacar senyum 😚  
    - 🎓 Target: Lulus dengan karya yang bisa bermanfaat!

    Terima kasih udah coba aplikasiku! 💖
    """)

# Footer
st.markdown("""
    <hr>
    <div style="text-align:center; font-size:13px; color:#aaa;">
        "Aplikasi hebat lahir dari niat tulus dan kopi hangat." ☕<br>
        Dibuat dengan 💕 oleh Desvita Sarhani Koly
    </div>
""", unsafe_allow_html=True)
