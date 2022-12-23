import streamlit as st

from Bible import Bible

my_bible = Bible()

my_bible.init()

def main():
    menu = ["Home", "Search by Book, Chapter, Verse", "Serch by Keyword", "About"]
    
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.warning("To Search by Book, Chapter, Verses, select the Menu Option 'Search by Book, Chapter, Verse' on the corner left upper side of the App. Thank You. God Bless You")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:

            st.write("Alejandra Mollo  21800242")

            st.title('Holy Bible')

            st.image("Holy-Bible.jpg", width=300)

        with col3:
            st.write(' ')
        
    elif choice == "Search by Book, Chapter, Verse":
        st.title("Handong Holy Bible")
        st.subheader("Verses Retrieval")
        
        st.info("Welcome to Holy Bible")
        books = my_bible.book_full_names
        book_names = st.selectbox("Select the Book", books)
        chapter = st.number_input("Chapter", 1)
        verse_max = my_bible.get_max_verse(book_names, chapter)
        verse = st.slider("Verse", 1, verse_max)
        
        text = my_bible.search(book_names, chapter, verse)

        st.write("Text")

        st.success(f"\n\n{text}\n\n")
        
        st.write("The verses of the day")

        text1 = my_bible.search("Genesis", 1, 1)
        text2 = my_bible.search("2 Peter", 1, 10)
        text3 = my_bible.search("Revelation", 2, 22)

        channel2 = f"\n\n{text1}\n\n{text2}\n\n{text3}\n"

        if(st.button("Click Here")):
            st.write("The Verses are:")
            
            st.error(f"{channel2}")
            
    elif choice == "Serch by Keyword":
        st.write("Enter Keyword to Search:")
        name = st.text_input("")
        if(st.button("Search")):
            found = my_bible.search_by_keyword(name)
            
            i = 0
            st.write("Search Results")
            for verse in found:
                if i < 10:
                    st.success(f'\n\n{verse}\n\n')
                    i += 1
         


    else:
        st.subheader("About the Handong Holy Bible")
        st.info("This Bible App was created by Alejandra Mollo Flores. For God so Loved the World, that he gave his only Son, that whoever believes in him should not perish but have eternal life. John 3:16 ESV.")
        
        
main()

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write("Copyright 2022 Alejandra Mollo Flores | Economist | Handong Global University")
