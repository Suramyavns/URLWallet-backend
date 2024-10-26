'''
This module specifies the entities and their attributes for the database
'''
from sqlalchemy import Column, Integer, String,UUID,ForeignKey
from database import Base
import random
import string

def generate_unique_string(length=10):
    """Generate a unique random string of fixed length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class Urls(Base):
    '''
    This entity will store url along with a primary key
    '''
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(10000))

    def __init__(self, id=None, url=None):
        self.id = id
        self.url = url

    def __repr__(self):
        return f'<URL {self.url} >'

class IDs(Base):
    '''
    This entity will store the IDs of each URL mapped to a UUID for security reasons
    '''
    __tablename__='ids'
    uuid = Column(String,primary_key=True,default=generate_unique_string)
    id = Column(Integer,ForeignKey('urls.id'),nullable=False)

    def __init__(self, uuid=None,url_id=None):
        self.uuid = uuid
        self.id = url_id

    def __repr__(self):
        return f'<ID {self.uuid} >'
