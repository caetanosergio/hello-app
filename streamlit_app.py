import streamlit as st

st.write("Alejandra Mollo  21800242")

st.title('Handong Bible App')

from Bible import Bible

my_bible = Bible()

my_bible.init()

st.info("This is an information")

st.warning("This is a warning")

st.error("An error occured")
t = my_bible.book_full_names

channel = f"{t}"

st.write("Subscribe to my channel", channel)

name = st.text_input("Enter the Bible name", "Bible Name")


st.button("Click here")

t = my_bible.book_full_names
print(t)

if(st.button("click here")):
    st.text(f"{st.write(f'{text}')}")


def main():
    st.title("Handong Holy Bible")
    menu = ["Home", "MultiVerse", "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Single Verse Search")

    elif choice == "MultiVerse":
        st.subheader("MultiVerse Retrieval")

    else:
        st.subheader("About")
        
        
main()

