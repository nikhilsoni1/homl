from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from variables import DATABASE_URI


class dbSession:
    def __init__(self, database_uri) -> None:
        self.database_uri = database_uri
        self.engine = None
        self.session = None

    def create_session(self):
        self.engine = create_engine(self.database_uri)
        session_maker = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        self.session = session_maker()
        return self.session
