from sqlalchemy import (
    Column,
    Integer,
    Text,
    Sequence,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class WebFormData(Base):
    __tablename__ = 'webformdata'
    id = Column(Integer, Sequence('webformdata_seq'), primary_key=True)
    title = Column(Text, unique=True)
    comment_text = Column(Text)

    def __init__(self, title, comment_text):
        self.title = title
        self.comment_text = comment_text
