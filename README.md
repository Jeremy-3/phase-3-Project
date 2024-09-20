# Phase-3-Project

## Online BookStore 📚

- A python project designed to manage authors and their books using SQLite database(Create,Read,Update,Delete)
  for both authors and books.The project also models a `one-to-many` relationship,where each author can have multiple books.

## Prerequisites

- Python 3.x
- SQLite3 

## Installation

1.Clone the repository:

        https://github.com/Jeremy-3/phase-3-Project.git


2 .Navigate to the directory 

       cd Phase3-project

3.Create the SQLite Database

- Ensure you have a `Bookstore.db` SQLite database file.If its not there type `python lib/seed.py`

4.Ensure you have python by running `python --version` o if not type `sudo apt install python`

5.Ensure you also have `sqlite3` by running `sqlite3 --version` if not 
`sudo apt install sqlite3` 

6.Ensure you launch your virtual environment in your command line by typing `pipenv shell` if an error occurs `pipenv install` then `pipenv shell`

7.Once your virtual environment has been creeated you can run `python lib/cli.py` to run the application.

8.Incase your missing the `ipdb` you can get it by `pip install ipdb` in your command line

## Project Features

- **Author Class**:

  - Add new authors
  - Update existing author information
  - Delete authors
  - Find authors by ID, name, or genre
  - List all authors

- **Book Class**:

  - Add new books associated with an author
  - Update book details
  - Delete books
  - Find books by ID, title, or year of publication
  - List all books

## Project Structure

- `_init_.py`:Creates a connection with the database.
- `models/`:Directory that contains the models for `Author` and `Book`
- `debug.py`:Used for debugging the data being passed to the data base.
- `cli.py`:The main program that handels user input and interactions with the system.
- `helpers.py`:Contains helper functions to handle operations like adding,updating,deleting and finding authors/books.
- `seed.py`:Creates the datbase and inserts the data given into it

## How to Use
Once you run the program(`python lib/cli.py`), you will see a menu of options to perform the following operations:

1.**List all authors**: 
Displays all the authors in the database.

2.**Find author by ID, name, or genre**: Search for an author based on different criteria.

3.**Add a new author**: Create a new author with a name and genre.

4.**Update author**: Modify the name or genre of an existing author.

5.**Delete author**: Permanently remove an author from the database.

6.**List all books**: Displays all the books in the database.

7.**Find book by ID, title, or year**: Search for a book based on different criteria.

8.**Add a new book**: Create a new book with a title, genre, year of publication, and associate it with an author.
9.**Update book**: Modify the details of an existing book.

10.**Delete book**: Permanently remove a book from the database.

## Lisence
This project is open-source and free to use.

## Authors
[Jeremy Gitau](https://github.com/Jeremy-3)
