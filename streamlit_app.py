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

st.write("Choose the verse", channel)

name = st.text_input("Enter the Bible name", "Bible Name")

option = st.selectbox("select the book", channel)

st.write("You Selected", option)

text1 = my_bible.search("Genesis", 1, 1)
text2 = my_bible.search("2 Peter", 1, 10)
text3 = my_bible.search("Revelation", 2, 22)

channel2 = f"\n\n{text1}\n\n{text2}\n\n{text3}\n"

st.write("The books are:", channel2)



st.button("Click here")

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

