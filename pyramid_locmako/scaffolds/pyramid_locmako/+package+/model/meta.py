from sqlalchemy import (
    Column,
    Integer,
    Text,

    engine_from_config,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value


def create_session(settings, prefix):
    engine = engine_from_config(settings, prefix)

    dbsession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
    dbsession.configure(bind=engine)

    return dbsession


