from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    """
    Represents a book with its details.

    Attributes:
        id (int): The unique identifier for the book.
        title (str): The title of the book.
        author (str): The author of the book.
        description (str): A brief description of the book.
        rating (int): The rating of the book.
        published_date (int): The year the book was published.
    """
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    """
    Represents a request to create or update a book.

    Attributes:
        id (Optional[int]): The unique identifier for the book (not needed in request).
        title (str): The title of the book (min length 3).
        author (str): The author of the book (min length 1).
        description (str): A brief description of the book (min length 1, max length 100).
        rating (int): The rating of the book (between 1 and 5).
        published_date (int): The year the book was published (between 2000 and 2030).
    """
    id: Optional[int] = Field(title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'codingwithroby',
                'description': 'A new description of a book',
                'rating': 5,
                'published_date': 2029
            }
        }

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    """
    Retrieve all books.
    Returns:
        list: A list of all books.
    """
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    """
    Retrieve a book by its ID.
    Args:
        book_id (int): The unique identifier for the book (greater than 0).
    Returns:
        dict: The details of the book with the given ID.
    Raises:
        HTTPException: If the book with the given ID is not found.
    """
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    """
    Retrieve books by their rating.
    Args:
        book_rating (int): The rating of the books to be retrieved (between 1 and 5).
    Returns:
        list: A list of books with the given rating.
    """
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    """
    Retrieve books by their published date.
    Args:
        published_date (int): The year the books were published (between 2000 and 2030).
    Returns:
        list: A list of books published in the given year.
    """
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    """
    Create a new book.
    Args:
        book_request (BookRequest): The details of the book to be created.
    Returns:
        dict: The details of the created book.
    """
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))
    return new_book

def find_book_id(book: Book):
    """
    Assign a new ID to the book.
    Args:
        book (Book): The book to be assigned a new ID.
    Returns:
        Book: The book with the assigned ID.
    """
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    """
    Update an existing book.
    Args:
        book (BookRequest): The details of the book to be updated.
    Raises:
        HTTPException: If the book with the given ID is not found.
    """
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    """
    Delete a book by its ID.
    Args:
        book_id (int): The unique identifier for the book (greater than 0).
    Raises:
        HTTPException: If the book with the given ID is not found.
    """
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')
