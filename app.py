import streamlit as st

# Инициализираме списъка в session_state, ако още не съществува
if 'books' not in st.session_state:
    st.session_state.books = [
        "The Hobbit",
        "1984",
        "Pride and Prejudice"
    ]

st.title("📚 Library Manager")

# Секция 1: Проверка на книга
st.subheader("Check Availability")
check_input = st.text_input("Enter title to search:")

if st.button("Check Book"):
    if any(b.lower() == check_input.strip().lower() for b in st.session_state.books):
        st.success(f"'{check_input}' is available!")
    else:
        st.error("Book not found.")

st.divider() # Визуална разделителна линия

# Секция 2: Добавяне на нова книга
st.subheader("Add New Book")
new_book = st.text_input("Enter new book title:")

if st.button("Add to Database"):
    clean_new = new_book.strip()
    if clean_new == "":
        st.warning("Please enter a title.")
    elif any(b.lower() == clean_new.lower() for b in st.session_state.books):
        st.info("This book is already in the database.")
    else:
        # Добавяме към списъка в session_state
        st.session_state.books.append(clean_new)
        st.success(f"Added '{clean_new}' successfully!")

# Опция: Показване на целия списък (за проверка)
if st.checkbox("Show all books"):
    st.write(sorted(st.session_state.books))
