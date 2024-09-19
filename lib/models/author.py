from models._init_ import CONN,CURSOR

class Author:
    
    def __init__(self,name,genre,id=None):
        self.id = id
        self.name = name
        self.genre = genre
        
    def __repr__(self):
        print (f"<Author {self.id}: {self.name} writes {self.genre}")
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def set_name(self,name):
        if isinstance(name,str) and len(name):
            self._name = name
        else:
            raise ValueError("Name cannot be an empty string !")    
    
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def set_genre(self,genre):
        if isinstance(genre,str) and len(genre):
            self._genre = genre
        else:
            raise ValueError("Genre cannot  not be an empty string !")  
        
    @classmethod
    def create_table(cls):
        sql='''
            CREATE TABLE IF NOT EXISTS authors(
                id INTEGER PRIMARY KEY,
                name TEXT,
                genre TEXT
            )
        '''      
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql='''
            DROP TABLE IF EXISTS authors;
        '''    
        CURSOR.execute(sql)
        CONN.commit()
        
    
    def save(self):
            sql='''
                INSERT INTO authors(name,genre)
                VALUES(?,?) 
            '''
            CURSOR.execute(sql,(self.name,self.hometown))
            CONN.commit()
            
    