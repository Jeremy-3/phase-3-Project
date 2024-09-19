from models._init_ import CONN,CURSOR
from models.author import Author
from models.book import Book

def seed_database():
    Author.drop_table()
    Author.create_table()
    Book.drop_table()
    Book.create_table()
     
     #seed data
    author1 = Author.create("J.k Rowling","Fantasy")
    book1 = Book.create("harry potter and the sorcerer's stone","fantasy",1997,author1.id) 
    

seed_database()
print("Database Created !!!")    