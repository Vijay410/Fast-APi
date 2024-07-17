from fastapi import FastAPI, HTTPException, Body  #import Fastapi from class
from fastapi.responses import JSONResponse

app = FastAPI()             #Intialize the app

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    '''
    Return hellow vijay as message
    '''
    try:
        print(BOOKS)
        if BOOKS is not None:
            return BOOKS
        else:
            raise HTTPException(status_code=404, detail="Books not found")
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, content={"message": e.detail})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'message': "An exception occuered"})

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    """
    Returns single book info
    arguments: takes argument book_title
    """
    for book in BOOKS:
        try:
            if book.get('title').casefold() == book_title.casefold():
                return book
        except Exception as e:
            raise HTTPException(status_code=500, detail="An unexpected error occurred")
    
    raise HTTPException(status_code=404, detail="Book not found")


@app.get('/books/')     
async def category_param_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/{books_author}')     
async def read_author_category_by_query(books_author:str, category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold() and \
            book.get('author').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

    
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book added successfully"}

@app.put("/books/update_book")
async def update_book(book_title:str, updated_book=Body()):
    for index, book in enumerate(BOOKS):
        print( book['title'], book_title)
        if book['title'].casefold() == book_title.casefold():
            BOOKS[index] == update_book
            return {"message": "Book updated succefully"}
    raise HTTPException(status_code=404, detail="Book not found")