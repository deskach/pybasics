from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from models.user import User
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', 
                           title = "Thermos",
                           user=User("Siarhei", "Kachanovich")
                           )

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)

@app.errorhandler(500)
def page_not_found(e):
    return (render_template('500.html'), 500)

@app.route('/add', methods=['GET', 'POST'])
def add():
    def store_bookmark(url):
        bookmarks.append({
            "url": url,
            "user": "reindert",
            "date": datetime.utcnow()
        })

    if request.method == "POST":
        url = request.form['url'] # url here is the input's name'
        store_bookmark(url)
        app.logger.debug('stored url: ' + url)

        return redirect(url_for('index'))
    
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True) 
