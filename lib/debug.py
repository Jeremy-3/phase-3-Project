from models._init_ import CONN,CURSOR
from models.author import Author


import ipdb
Author.drop_table()
Author.create_table()



ipdb.set_trace()