#!/usr/local/bin/python3

from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Author, Book

# connection with sqlite database
engine = create_engine('sqlite:///books_authors.db', echo=True)

# get sesion
Session = sessionmaker(bind=engine)
session = Session()

# inserting authors
author_1 = Author('Author1')
author_2 = Author('Author2')
author_list = (author_1, author_2)
session.add_all(author_list)
session.commit()

# inserting books
book1 = Book('Book1', date(2019, 1, 1), '123456789')
book1.authors.append(author_1)
session.add(book1)
session.commit()

# book query
book = session.query(Book).filter(Book.isbn=='123456789').first()
print(book)

# modifying book data
book.title = 'Learning Python Networking'
session.commit()

print(book)