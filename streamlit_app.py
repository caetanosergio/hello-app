import streamlit as st

st.write("Alejandra Mollo  21800242")

st.title('Handong Bible App')

from Bible import Bible

my_bible = Bible()

my_bible.init()

st.info("This is an information")

st.warning("This is a warning")

st.error("An error occured")

channel = "iakdskjfdkj"

st.write("Subscribe to my channel", channel)
