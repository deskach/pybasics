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

if __name__ == '__main__':
    app.run(debug=True) 
