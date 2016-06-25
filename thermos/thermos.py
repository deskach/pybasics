from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from models.user import User
from logging import DEBUG
from forms import BookmarkForm

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '>\x8e\xaf}\x11`n\xd62\x8a\x98>a\x0b\xe1\x1d-V\x00\xa0^\xff[\xcb\xaa'

bookmarks = []

@app.route('/')
@app.route('/index')
def index():
    def new_bookmarks(num):
        return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

    return render_template('index.html', 
                           title = "Thermos",
                           user=User("Siarhei", "Kachanovich"),
                           new_bookmarks=new_bookmarks(5)
                           )

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)

@app.errorhandler(500)
def page_not_found(e):
    return (render_template('500.html'), 500)

@app.route('/add', methods=['GET', 'POST'])
def add():
    def store_bookmark(url, description=""):
        bookmarks.append({
            "url": url,
            "description": description,
            "user": "reindert",
            "date": datetime.utcnow()
        })
    
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
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

if __name__ == '__main__':
    app.run(debug=True) 
