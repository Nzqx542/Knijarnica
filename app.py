import streamlit as st

if 'books' not in st.session_state:
    st.session_state.books = ["The Hobbit", "1984", "The Great Gatsby"]

st.title("Book Manager")

# Проверка на книга
check_input = st.text_input("Search book:")
if st.button("Check"):
    if any(b.lower() == check_input.strip().lower() for b in st.session_state.books):
        st.success("Found!")
    else:
        st.error("Not found.")

# Добавяне на книга
add_input = st.text_input("Add new book:")
if st.button("Add"):
    if add_input.strip() and add_input not in st.session_state.books:
        st.session_state.books.append(add_input.strip())
        st.success("Added!")

# Списък
if st.checkbox("Show Library"):
    st.write(st.session_state.books)
