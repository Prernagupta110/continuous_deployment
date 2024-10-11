from .models import Book

books_db = []

def create_book(book: Book):
    books_db.append(book)
    return book

def get_books(author: str = None):
    if author:
        return [book for book in books_db if book.author == author]
    return books_db

def get_book(book_id: str):
    return next((book for book in books_db if book.id == book_id), None)

def update_book(book_id: str, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    return None

def delete_book(book_id: str):
    global books_db
    books_db = [book for book in books_db if book.id != book_id]
