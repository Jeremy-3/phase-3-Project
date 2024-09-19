from models._init_ import CONN,CURSOR

class Author:
    
    all = {}
    
    def __init__(self,name,genre,id=None):
        self.id = id
        self.name = name
        self.genre = genre
        
    def __repr__(self):
        return f"<Author {self.id}: {self.name} writes {self.genre}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name):
            self._name = name
        else:
            raise ValueError("Name cannot be an empty string !")    
    
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self,genre):
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
            CURSOR.execute(sql,(self.name,self.genre))
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
            
    @classmethod
    def create(cls,name,genre):
        author =cls(name,genre)
        author.save()
        return author
    
    def update(self):
        sql='''
            UPDATE authors
            SET name = ?,
            genre = ? 
            WHERE id = ? 
        '''
        CURSOR.execute(sql,(self.name,self.genre,self.id))
        CONN.commit()
    
    def delete(self):
        sql='''
            DELETE FROM authors 
            WHERE id = ?
        ''' 
        CURSOR.execute(sql,(self.id))
        CONN.commit()   
        
        del type(self).all[self.id]
        self.id = None
        
    
    @classmethod
    def all_instances(cls,row):
        author = cls.all.get(row[0])
        if author:
            author.name=row[1]
            author.genre=row[2]
        else:
            author=cls(row[1],row[2])
            author.id = row[0]
            cls.all[author.id] = author
        return author        
    
    
    @classmethod
    def get_all(cls):
        sql='''
            SELECT * FROM authors
        '''
        
        rows = CURSOR.execute(sql).fetchall()
        
        return [cls.all_instances(row) for row in rows]
   