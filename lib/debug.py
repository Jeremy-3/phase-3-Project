from models._init_ import CONN,CURSOR
from models.author import Author
from models.book import Book


import ipdb
Author.drop_table()
Author.create_table()
Book.drop_table()
Book.create_table()


ipdb.set_trace()