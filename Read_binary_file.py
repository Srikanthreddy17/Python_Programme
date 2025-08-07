import pickle
# Open a file in binary read mode and load the list of books
with open("books.dat", "rb") as file:
    # Load the list of books from the file
    books = pickle.load(file)
    # Print the details of each book
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")