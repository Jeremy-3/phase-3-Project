from models.author import Author
from models.book import Book

def exit_program():
    print("Thank you for visiting Come again 👋")
    exit()
    
#author functions to be implemented
    
def list_authors():
    print("Listing all authors in store....")
    authors = Author.get_all()
    for authors in authors:
        print(authors)
    print("Here They are..")    

def find_author_by_id():
    print("Getting  id....")
    id = input("Enter the Authors id:")
    author = Author.find_by_id(id)
    if author:
        print(author)
    else:
        print(f"Apologies the ID:{id} of Author has not been found ! ")
        
def find_author_by_name():
    print("Getting name...")
    name = input('Enter Authors name here: ')
    author = Author.find_by_name(name)
    if author:
        print(author)
    else:
        print(f'Author {name} has not been found !')    

def find_author_by_genre():
    print("Getting genre...")
    genre = input('Enter the genre the Author writes:')
    author = Author.find_by_genre(genre)
    if author:
        print(author)
    else:
        print(f'{genre} has not been found !')    

def create_new_author():
    print("New Author....")
    name = input("Enter Author's name:")
    genre = input("Enter the genre written: ")
    try:
        author = Author.create(name,genre)
        print(f'Success:{author}')
    except Exception as exc:
        print("Some Error has occurred during entry please try again:",exc)    

def update_author():
    print("Making Updates...")
    id = input("Enter the Author's id you wish to update:")
    if author:=Author.find_by_id(id):
        try:
            name=input("Enter the author's new name:")
            author.name=name
            genre = input("Enter Author's new genre:")
            author.genre = genre
        except Exception as exc:
            print("Error in updating Author kindly check your input and try again:",exc)
            
def delete_author():
    print('Making deletion...')
    id = input("Enter Author's id:")
    if author := Author.find_by_id(id):
        author.delete()
        print(f"Author {id} has been DELETED!")
    else:
        print(f"Author {id} not found !")    
        

#book functions to be implemented

def list_books():
    print("Getting all books...")
    books = Book.get_all()
    for books in books:
        print(books)
    print("Here are your books enjoy!")    

def find_book_by_id():
    print("Getting id...")
    id = input("Enter Book's id:")
    book = Book.find_by_id(id)
    if book:
        print(book)
    else:
        print(f"Sorry we cannot find book ID of {id}")
            

def find_book_by_title():
    print("Getting Title...")
    title = input("Enter Book's Title: ")
    book = Book.find_by_title(title)
    if book:
        print(book)
    else:
        print(f"We cannot seem to find a book titled {title} ")
            

def find_book_by_year_published():
    print("Getting Year of publish....")
    year_published = input("Enter the published year of the book:")
    book = Book.find_by_year(year_published)
    if book:
        print(book)
    else:
        print(f"{year_published} cannot be found !")
            
        
def create_new_book():
    print("Adding a new book....")
    title = input("Enter Book's title:")
    genre = input("Enter Book's genre:")
    
    try:
        year_published = int(input("Enter year of publish:"))
        author_id=int(input("Enter the Author's id:"))
        
        book = Book.create(title,genre,year_published,author_id)
        print(f'Success:{book}')
    except Exception as exc:
        print("Error found Check your inputs and confirm again:",exc)
             

def update_book():
    print("Getting Updates....")
    id = input("Enter Book's ID for updates")
    if book := Book.find_by_id(id):
        try:
            title = input("Enter book's new title:")
            book.title=title
            genre = input("Enter book's new genre:")
            book.genre = genre
            year_published=input("Enter book's new year of publish:")
            book.year_published = year_published
            author_id=input("Enter book's new Author Id:")
            book.author_id = author_id
            
            book.update()
            print(f"Success{book}")
        except Exception as exc:
            print("Error caught during update kindly check your inputs:",exc)
            
            
def delete_book():
    print("Marking Deletion...")
    id = input("Enter the Book's ID you wish to terminate:")
    if book := Book.find_book_by_id(id):
        book.delete()
        print(f"Book {id} has been deleted")
    else:
        print(f"{id} has not been found")    

      