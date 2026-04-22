import streamlit as st
import random

st.title("Şifre Oluşturucu")

karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

if st.button("Oluştur"):
    sifre = ""
    for i in range(8):
        sifre += random.choice(karakterler)

    st.write("Şifreniz:", sifre)
    st.balloons()