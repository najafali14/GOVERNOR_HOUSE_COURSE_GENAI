import streamlit as st
import json

# Library management class
class Library:
    def __init__(self):
        self.books = []
        self.load_library('library.json')

    def add_book(self, title, author, publication_year, genre, read_status):
        book = {
            'title': title,
            'author': author,
            'publication_year': publication_year,
            'genre': genre,
            'read_status': read_status
        }
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book['title'].lower() != title.lower()]

    def search_books(self, search_type, search_term):
        if search_type == "Title":
            return [book for book in self.books if search_term.lower() in book['title'].lower()]
        elif search_type == "Author":
            return [book for book in self.books if search_term.lower() in book['author'].lower()]
        return []

    def display_books(self):
        return self.books

    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book['read_status'])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
        return total_books, percentage_read

    def save_library(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def load_library(self, filename):
        try:
            with open(filename, 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []


# Initialize Library instance
library = Library()

# Streamlit App layout
st.title("Personal Library Manager")

menu = ["Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics", "Exit"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add a book":
    st.subheader("Add a New Book")

    title = st.text_input("Enter the book title")
    author = st.text_input("Enter the author")
    publication_year = st.number_input("Enter the publication year", min_value=1000, max_value=2025)
    genre = st.text_input("Enter the genre")
    read_status = st.radio("Have you read this book?", ("Yes", "No"))

    if st.button("Add Book"):
        if title and author and genre:
            library.add_book(title, author, publication_year, genre, read_status == "Yes")
            library.save_library('library.json')
            st.success(f"Book '{title}' added successfully!")
        else:
            st.error("Please fill out all fields.")

elif choice == "Remove a book":
    st.subheader("Remove a Book")
    title_to_remove = st.text_input("Enter the title of the book to remove")

    if st.button("Remove Book"):
        if title_to_remove:
            library.remove_book(title_to_remove)
            library.save_library('library.json')
            st.success(f"Book '{title_to_remove}' removed successfully!")
        else:
            st.error("Please enter a book title to remove.")

elif choice == "Search for a book":
    st.subheader("Search for a Book")
    search_type = st.radio("Search by", ("Title", "Author"))
    search_term = st.text_input(f"Enter the {search_type.lower()} to search")

    if st.button("Search"):
        if search_term:
            results = library.search_books(search_type, search_term)
            if results:
                for i, book in enumerate(results, 1):
                    status = "Read" if book['read_status'] else "Unread"
                    st.write(f"{i}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")
            else:
                st.write(f"No books found matching {search_type} '{search_term}'")
        else:
            st.error(f"Please enter a {search_type.lower()} to search.")

elif choice == "Display all books":
    st.subheader("All Books in Your Library")
    books = library.display_books()
    if books:
        for i, book in enumerate(books, 1):
            status = "Read" if book['read_status'] else "Unread"
            st.write(f"{i}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")
    else:
        st.write("Your library is empty.")

elif choice == "Display statistics":
    st.subheader("Library Statistics")
    total_books, percentage_read = library.display_statistics()
    st.write(f"Total books: {total_books}")
    st.write(f"Percentage read: {percentage_read:.2f}%")

elif choice == "Exit":
    library.save_library('library.json')
    st.write("Library saved to file. Goodbye!")
