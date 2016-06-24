from flask import Flask, render_template, url_for
from models.user import User

app = Flask(__name__)


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

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True) 
