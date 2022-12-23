import streamlit as st

st.write("Alejandra Mollo  21800242")

st.title('Handong Bible App')

from Bible import Bible

my_bible = Bible()

my_bible.init()
