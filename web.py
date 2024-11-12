

import streamlit as st
from PIL import Image


# st.set_page_config(page_title="Portfolio", layout="wide")


col1, col2 = st.columns([2, 3.8])  # Menentukan lebar kolom

# Kolom kiri untuk judul
with col1:
    st.header(''' :grey[Portofo]:red[lio]''')

# Kolom tengah untuk tombol navigasi
with col2:
    st.write("")
    col1, col2, col3, col4, col5 = st.columns(5)  # 5 kolom untuk tombol

    # Menambahkan tombol navigasi di setiap kolom
    with col1:
        if st.button("Home"):
            st.write("Home page clicked!")
    with col2:
        if st.button("About"):
            st.write("About Me page clicked!")
    with col3:
        if st.button("Skills"):
            st.write("Skills page clicked!")
    with col4:
        if st.button("Projec"):
            st.write("Services page clicked!")
    with col5:
        if st.button("Contact"):
            st.write("Contact Us page clicked!")
st.markdown('___')


# Konten lain di bawah header

colom1, colom2  = st.columns([3,2])  

with colom1 :
    st.header("")
    st.markdown('''#### _:red[hello], my :grey[name] is_''')
    st.markdown("# Muhammad Muhsin")
    st.markdown("### :grey[I'am Web Developer]")
    st.header("")
with colom2:
    st.empty()
    img = Image.open("fotoprofil.png")
    st.image(img)
    st.empty()

st.markdown('___')

# KOnten
st.header("Abaut :red[Me]")
st.markdown('''Halo!, Saya seorang pengembang web yang berfokus pada pembuatan situs web yang responsif 
            dan mudah digunakan. Dengan pengalaman di berbagai teknologi web, saya berkomitmen untuk 
            menciptakan pengalaman pengguna yang menyenangkan dan solusi yang efisien untuk berbagai 
            kebutuhan bisnis. Saya senang bekerja dengan teknologi terkini dan selalu berusaha untuk 
            mengembangkan keterampilan saya agar dapat memberikan hasil terbaik.
            
Keahlian saya meliputi pengembangan front-end dan back-end, serta penerapan desain yang 
adaptif dan fungsional. Saya juga memiliki pemahaman yang kuat tentang pengembangan aplikasi
berbasis web yang dapat berjalan lancar di berbagai platform..''')

st.markdown('___')

st.header(":red[My] Skills")

st.markdown("Halo!, Saya seorang pengembang web yang berfokus pada pembuatan situs web yang responsif dan mudah digunakan. Dengan pengalaman di berbagai teknologi web, saya berkomitmen untuk menciptakan pengalaman pengguna yang menyenangkan dan solusi yang efisien untuk berbagai kebutuhan bisnis. Saya senang bekerja dengan teknologi terkini dan selalu berusaha untuk mengembangkan keterampilan saya agar dapat memberikan hasil terbaik. Keahlian saya meliputi pengembangan front-end dan back-end, serta penerapan desain yang adaptif dan fungsional. Saya juga memiliki pemahaman yang kuat tentang pengembangan aplikasi berbasis web yang dapat berjalan lancar di berbagai platform..")



st.markdown('___')
# Menampilkan judul utama
st.header("Pro:red[jects]")

# Membuat layout dengan 3 kolom untuk menampilkan proyek secara sejajar
col1, col2, col3 = st.columns(3)

# Kartu Proyek A
with col1:
    st.button(":red[PROJEC A]")
    st.write("**Description**: A simple web app built using Flask for task management. The app allows users to add, remove, and update tasks.")
    
# Kartu Proyek B
with col2:
    st.button(":red[PROJEC B]")
    st.write("**Description**: A data analysis project utilizing Python and Pandas. This project analyzes sales data to uncover trends and insights.")
    
# Kartu Proyek C
with col3:
    st.button(":red[PROJEC C]")
    st.write("**Description**: An e-commerce site built with Django. This site includes a product catalog, shopping cart, and checkout functionality.")
st.markdown('___')



# Fungsi untuk membuka URL saat ikon ditekan
st.header("Contact")

# URL yang ingin dibuka
kolom1, kolom2, kolom3 =st.columns([1,1,1])

# Tombol link sederhana yang disamarkan
with kolom1:
    img = Image.open("instagram.png")
    st.image(img, width= 60)
    st.write(f"[:red[Instangram]](https://www.instagram.com/mad_muhsin/)")
# Tombol link sederhana yang disamarkan
with kolom2:
    img = Image.open("dribbble.png")
    st.image(img, width=60)
    st.write(f"[:red[facebook]](https://www.example.com)")

# Tombol link sederhana yang disamarkan
with kolom3:
    img = Image.open("facebook.png")
    st.image(img, width=60)
    st.write(f"[:red[Github]](https://www.example.com)")
