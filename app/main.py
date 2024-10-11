from fastapi import FastAPI, HTTPException
from .models import Book, Success, Error
from .crud import create_book, get_books, get_book, update_book, delete_book

app = FastAPI()

# Create a new book
@app.post("/book", response_model=Success)
def create_book_endpoint(book: Book):
    created_book = create_book(book)
    return {"message": "Book created", "id": created_book.id}

# Get list of books
@app.get("/books")
def get_books_endpoint(author: str = None):
    return get_books(author)

# Get a specific book by ID
@app.get("/book/{book_id}", response_model=Book)
def get_book_endpoint(book_id: str):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update a specific book by ID
@app.put("/book/{book_id}", response_model=Success)
def update_book_endpoint(book_id: str, updated_book: Book):
    book = update_book(book_id, updated_book)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book updated", "id": book_id}

# Delete a specific book by ID
@app.delete("/book/{book_id}", status_code=204)
def delete_book_endpoint(book_id: str):
    delete_book(book_id)
