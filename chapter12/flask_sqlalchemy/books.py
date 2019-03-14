#!/usr/local/bin/python3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from datetime import date

# Flask application and config
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# Model
class Book(db.Model):
    __tablename__ = 'Book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(255))
    author = db.Column(db.Unicode(255))
    date = db.Column(db.DateTime())
    description = db.Column(db.Text())

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description
        self.date = date.today()

# Flask Form
class CreateBookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])

@app.route('/new_book', methods=['POST'])
def new_book():
    form = CreateBookForm()
    if request.method == 'POST':
        post = Book(request.form['title'], request.form['author'],request.form['description'])
        db.session.add(post)
        db.session.commit()
        # validate the received values
        if request.form['title'] and request.form['author']:
            return json.dumps({'html':'<span>New book saved in database</span>'})
    return render_template('index.html',form = form,conf = app.config)


@app.route('/', methods=['GET'])
def index():
    form = CreateBookForm()
    return render_template('index.html',form = form,conf = app.config)

if __name__ == '__main__':
    app.run()
    db.create_all()