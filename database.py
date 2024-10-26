'''
This module creates the database instance for this server
'''
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv
import pymysql

pymysql.install_as_MySQLdb()

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


engine = create_engine(os.getenv('dburl'),
    pool_size=10,          # Default is usually 5
    max_overflow=20,       # Allows for temporary connections above the pool_size
    pool_timeout=30,       # Time to wait for a connection to become available
    pool_pre_ping=True)
logger.info('Database connection established')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    '''
    import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db()
    '''
    import models
    Base.metadata.create_all(bind=engine)
