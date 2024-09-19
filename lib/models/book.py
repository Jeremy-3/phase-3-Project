from models._init_ import CONN,CURSOR

class Book:
    def __init__(self,title,genre,year_published,author_id,id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.year_published = year_published
        self.author_id = author_id
        
    def __repr__(self):
        return f"<Book {self.id} title:{self.title} genre:{self.genre} year:{self.year_published} Author is{self.author_id}>"
        
    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self,title):
        if isinstance(title,str) and len(title):
            self._title = title.title()
        else:
            raise ValueError("Title cannot be an empty string !")
        
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self,genre):
        if isinstance(genre,str) and len(genre):
            self._genre = genre
        else:
            raise("Genre cannot be an empty string !") 
    
    @property
    def year_published(self):
        return self._year_published
    
    @year_published.setter
    def year_published(self,year_published):
        if not isinstance(year_published,int):
            raise TypeError("Year must be an integer")
        elif year_published < 0 :
            raise ValueError("Year cannot be negative")
        else:
            self._year_published = year_published
        
    @classmethod
    def create_table(cls):
        sql='''
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                title TEXT,
                genre TEXT,
                year_published INTEGER,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id)
            )
        '''      
        CURSOR.execute(sql)
        CONN.commit()
     
    @classmethod
    def drop_table(cls):
        sql='''
            DROP TABLE IF EXISTS books;
        ''' 
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql='''
            INSERT INTO books(title,genre,year_published,author_id)
            VALUES(?,?,?,?) 
        '''
        CURSOR.execute(sql,(self.title,self.genre,self.year_published,self.author_id))
        CONN.commit()
        self.id = CURSOR.lastrowid          
    
    @classmethod
    def create(cls,title,genre,year_published,author_id):
        book = cls(title,genre,year_published,author_id)
        book.save()
        return book    
    
    
    def update(self):
        sql='''
            UPDATE books
            SET title = ? ,genre = ?,year_published = ?,author_id = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql,(self.title,self.genre,self.year_published,self.author_id,self.id))
        CONN.commit()
    
    def delete(self):
        sql='''
           DELETE FROM books 
           WHERE id = ?  
        '''    
        CURSOR.execute(sql,(self.id))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None