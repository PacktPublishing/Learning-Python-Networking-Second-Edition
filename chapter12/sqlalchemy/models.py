#!/usr/local/bin/python3

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///books_authors.db', echo=True)
Base = declarative_base()

#Relation many to many between book and author
author_book = Table('author_book', Base.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('author_id', Integer, ForeignKey('author.id'))
)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(120), index=True, nullable=False)
    date = Column(Date)
    isbn = Column(String(13))
    authors = relationship("Author", secondary=author_book)

    def __init__(self, title, date, isbn):
        self.title = title
        self.date = date
        self.isbn = isbn

    def __repr__(self):
        return self.title


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)

    def __init__(self, name):
        self.name = name


Base.metadata.create_all(engine)