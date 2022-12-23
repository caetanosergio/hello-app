import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.write("Alejandra Mollo  21800242")
    
    st.title('Handong Bible App')

    st.image("Holy-Bible.jpg", width=300)

with col3:
    st.write(' ')

from Bible import Bible

my_bible = Bible()

my_bible.init()

st.info("This is an information")

st.warning("This is a warning")

st.error("An error occured")
t = my_bible.book_full_names

channel = f"{t}"

st.write("Choose the verse", channel)

name = st.text_input("Enter the Bible name", "The verse of the day is")

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
    
    books = my_bible.book_full_names
    

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Single Verse Search")
        
        book_names = st.sidebar.selectbox("select the book", books)
        chapter = st.sidebar.number_input("Chapter", 1)
        verse = st.sidebar.number_input("Verse", 1)
        st.sidebar.write("You Selected", book_names)

    elif choice == "MultiVerse":
        st.subheader("MultiVerse Retrieval")

    else:
        st.subheader("About")
        
        
main()

