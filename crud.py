'''
This module will handle the necessary CRUD operations of the server
'''
from uuid import UUID
import validators
from database import db_session
from models import Urls,IDs

def add_url(url):
    '''
    This method will create a url object in the database.
    Return uuid
    '''
    if validators.url(url):
        obj = Urls(url=url)
        db_session.add(obj)
        db_session.flush()
        data = IDs(url_id=obj.id)
        db_session.add(data)
        db_session.commit()
        return data.uuid
    return None

def get_url(uuid):
    '''
    This method will retrieve the url from the provided uuid
    Returns url string
    '''
    try:
        urlid = db_session.get(IDs,uuid)
    except:
        return None
    if urlid:
        urlobj = db_session.get(Urls,urlid.id)
        return urlobj.url
    return None
