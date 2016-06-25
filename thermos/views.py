from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for

from thermos import app, db
from forms import BookmarkForm
from models import User, Bookmark

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', 
                           title = "Thermos",
                           new_bookmarks=Bookmark.new_bookmarks(5)
                           )

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)

@app.errorhandler(500)
def page_not_found(e):
    return (render_template('500.html'), 500)

@app.route('/add', methods=['GET', 'POST'])
def add():    
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("stored url: '%s'" % url)

        return redirect(url_for('index'))    

    return render_template('add.html', form=form)

    # if request.method == "POST":
    #     url = request.form['url'] # url here is the input's name'
    #     store_bookmark(url, description)
    #     app.logger.debug('stored url: ' + url)
    #     flash("stored url: '%s'" % url)

    #     return redirect(url_for('index'))

    # return render_template('add.html')
