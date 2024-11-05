import streamlit as st

# Informasi Umum
st.title("Portfolio Muhammad Muhsin")
st.subheader("Data Scientist | Developer | Enthusiast")
st.write("""
Selamat datang di portofolio saya! Di sini Anda dapat menemukan informasi mengenai latar belakang, proyek, 
dan keahlian saya.
""")

# Tentang Saya
st.header("Tentang Saya")
st.write("""
Halo! Saya Muhammad Muhsin, seorang developer yang gemar bereksperimen dengan teknologi terbaru. 
Saya berpengalaman dalam mengembangkan aplikasi IoT menggunakan Arduino, khususnya proyek-proyek seperti 
drum MIDI dan perangkat pintar. Saya juga memiliki dasar yang kuat dalam ilmu data dan matematika diskrit.
""")

# Keahlian
st.header("Keahlian")
skills = {
    "Bahasa Pemrograman": ["Python", "C++", "JavaScript"],
    "Framework & Tools": ["Streamlit", "Arduino", "TensorFlow", "Pandas"],
    "Keterampilan Lainnya": ["Analisis Data", "Pemrograman IoT", "Machine Learning"]
}

for skill, items in skills.items():
    st.subheader(skill)
    st.write(", ".join(items))

# Pengalaman Proyek
st.header("Proyek")
st.subheader("1. Arduino Drum MIDI")
st.write("""
Proyek ini menggunakan Arduino Leonardo Pro Micro dan 12 pad piezo untuk membuat MIDI controller. 
Menggunakan library Hello Drum, proyek ini memungkinkan pengguna untuk menghasilkan nada dengan memukul pad drum.
""")

st.subheader("2. Sistem Pengontrol LED IoT")
st.write("""
Proyek IoT yang memungkinkan pengguna mengontrol LED dari jarak jauh menggunakan aplikasi web. Menggunakan 
Arduino dan modul WiFi ESP8266 untuk terhubung dengan server.
""")

# Kontak
st.header("Kontak")
st.write("Jika tertarik dengan proyek atau ingin bekerja sama, silakan hubungi saya di:")
st.write("- **Email:** muhsin@example.com")
st.write("- **LinkedIn:** [linkedin.com/in/muhammadmuhsin](https://www.linkedin.com/in/muhammadmuhsin)")
st.write("- **github:** [MUHAMMAD MUHSIN](https://github.com/muhsin230105)")

# Footer
st.write("Terima kasih telah mengunjungi portofolio saya!")
