import streamlit as st

st.write("Hello World")


# Title
st.title('Handong Bible App')

# Header
st.header("This is the Heading")

# Subh
st.subheading("This is the subheading")

#text
st.text("Hello this is Ale's Bible")

# success, info
st.sucess("Executed successfully")
st.info("This is an information")
st.warning("This is a warning")
st.error("An error occured")
channel = "iakdskjfdkj"
st.write("Subscribe to my channel", channel)

#Text input box
name = st.text_input("Enter the Bible name", "Bible Name")
