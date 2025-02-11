# FastAPI Book API

This project is a simple Book API built with FastAPI.

## Overview

The Book API allows you to manage a collection of books. You can perform the following operations:
- Retrieve all books
- Retrieve a book by ID
- Retrieve books by rating
- Retrieve books by publish date
- Create a new book
- Update an existing book
- Delete a book by ID

## Installation

To install and run this project, follow these steps:

1. Clone the repository:

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

## Usage

Once the server is running, you can access the API at `http://127.0.0.1:8000`.

### Endpoints

#### Get All Books
- **URL:** `/books`
- **Method:** `GET`
- **Response:** List of all books

#### Get Book by ID
- **URL:** `/books/{book_id}`
- **Method:** `GET`
- **Path Parameter:** `book_id` (int) - ID of the book
- **Response:** Book details

#### Get Books by Rating
- **URL:** `/books/`
- **Method:** `GET`
- **Query Parameter:** `book_rating` (int) - Rating of the books to retrieve
- **Response:** List of books with the specified rating

#### Get Books by Publish Date
- **URL:** `/books/publish/`
- **Method:** `GET`
- **Query Parameter:** `published_date` (int) - Year of publication
- **Response:** List of books published in the specified year

#### Create a New Book
- **URL:** `/create-book`
- **Method:** `POST`
- **Request Body:** BookRequest object
- **Response:** Created book details

#### Update a Book
- **URL:** `/books/update_book`
- **Method:** `PUT`
- **Request Body:** BookRequest object
- **Response:** No content

#### Delete a Book
- **URL:** `/books/{book_id}`
- **Method:** `DELETE`
- **Path Parameter:** `book_id` (int) - ID of the book to delete
- **Response:** No content

## Automatic API Documentation

You can access the interactive API documentation generated by FastAPI at the following URLs:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
