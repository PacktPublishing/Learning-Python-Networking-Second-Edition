#!/usr/local/bin/python3

import os
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(os.path.dirname(__file__), 'books_database.db')
SECRET_KEY = 'SECRET_KEY'