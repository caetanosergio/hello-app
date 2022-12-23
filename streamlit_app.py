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

name = st.text_input("Enter the Bible name", "Bible Name")

book, chapter, verse = name.split(name)

text = my_bible.search(book, int(chapter), int(verse))

st.button("Click here")

t = my_bible.book_full_names
print(t)

if(st.button("click here")):
    st.text(f"{st.write(text)}")


