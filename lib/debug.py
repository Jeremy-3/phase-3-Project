from models._init_ import CONN,CURSOR
from models.author import Author
from models.book import Book

import ipdb
def reset_database():
    Author.drop_table()
    Author.create_table()
    Book.drop_table()
    Book.create_table()
    
    #seed data
    author1 = Author.create("J.k Rowling","fantasy")
    book1 = Book.create("harry potter and the sorcerer's stone","fantasy",1997,author1.id) 
    author2 = Author.create("Mary Shelly","Horror")
    book2 =Book.create("frankensten","Horror",1818,author2.id)
    author3 = Author.create("Toni Mark","Adventure")
    book3=Book.create("Beloved","fantasy",1945,author1.id)
    book4 = Book.create("one hundred","Adventure",1979,author3.id)
    book5 = Book.create("lord of the rings","Adventure",1954,author3)
    


reset_database()
ipdb.set_trace()