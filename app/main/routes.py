from flask import Blueprint, redirect, render_template, url_for
from app import db
from app.models import *
from app.main.forms import AddAuthorForm,AddBookForm



main_blueprint = Blueprint('main',__name__,url_prefix='/')


# home page (all books)
@main_blueprint.route('/',endpoint='books',methods=['GET'])
def books():
    data = db.session.query(Book).all()
    for book in data:
        author = db.session.query(Author).filter(Author.id == book.author_id).first()
        book.author = author.name
    return render_template('books.html', books=data)

# book details
@main_blueprint.route('/books/<int:book_id>',endpoint='book_details',methods=['GET'])
def book_details(book_id):
    data = db.session.query(Book).filter(Book.id == book_id).first()
    author = db.session.query(Author).filter(Author.id == data.author_id).first()
    data.author = author.name
    print(data.image_url)
    return render_template('BookDetails.html', book=data)


# author details
@main_blueprint.route('/authors/<int:author_id>',endpoint='author_details',methods=['GET'])
def author_details(author_id):
    data = db.session.query(Author).filter(Author.id == author_id).first()
    books = db.session.query(Book).filter(Book.author_id == author_id).all()
    data.books = books
    return render_template('AuthorDetails.html', author=data)


# adding new author
@main_blueprint.route('/authors/',endpoint='add_author',methods=['POST'])
def add_author():
    form = AddAuthorForm()
    if form.validate_on_submit():
        new_author = Author(
            name=form.name.data)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('add_author.html', form=form)

# adding new book
@main_blueprint.route('/books/',endpoint='add_book',methods=['POST'])
def add_book():
    form = AddBookForm()
    form.author.choices = [(author.id, author.name) for author in Author.query.all()]
    if form.validate_on_submit():
        new_book = Book(
            name=form.name.data,
            publish_date=form.publish_date.data,
            price=float(form.price.data),
            age_category=form.age_category.data,
            image_url=form.image_url.data,
            author_id=form.author.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('add_book.html', form=form)

# update book
@main_blueprint.route('/books/<int:book_id>',endpoint='update_book',methods=['POST'])
def update_book(book_id):
    form = AddBookForm()
    form.author.choices = [(author.id, author.name) for author in Author.query.all()]
    if form.validate_on_submit():
        book = db.session.query(Book).filter(Book.id == book_id).first()
        book.name = form.name.data
        book.publish_date = form.publish_date.data
        book.price = float(form.price.data)
        book.age_category = form.age_category.data
        book.author_id = form.author.data
        db.session.commit()
        return redirect(url_for('main.books'))
    return render_template('update_book.html', form=form)


@main_blueprint.route('/book/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('main.books'))



@main_blueprint.route('/author/update/<int:author_id>', methods=['GET', 'POST'])
def update_author(author_id):
    author = Author.query.get_or_404(author_id)
    form = AddAuthorForm(obj=author)
    if form.validate_on_submit():
        author.name = form.name.data
        db.session.commit()
        return redirect(url_for('main.books'))
    return render_template('update_author.html', form=form, author=author)


@main_blueprint.route('/author/delete/<int:author_id>', methods=['POST'])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('main.books'))
