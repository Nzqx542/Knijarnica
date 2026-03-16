import streamlit as st

books = [
  "The Hobbit",
  "1984",
  "Pride and Prejudice",
  "To Kill a Mockingbird",
  "The great Gatsby",
  "Withering Heights"
]

st.title("book Checker app")
st.write("Enter a book title to check if it exists in the database")

user_input = st.text_input("Book Title: ")

if st.button("Check Book"):
  if user_input.strip() == "":
    st.warning("Please enter a book title.")
  elif user_input in books: 
    st.success("The book exists in the database!")
  else:
    st.error("The book is not in the database!")

new_book = st.text_input("Add a new book:")
if st.button("Add"):
    books.append(new_book)
    st.success(f"Added {new_book} (temporarily)")
