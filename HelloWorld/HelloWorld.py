from flask import Flask

app = Flask(__name__) # a global flask application module

# functions and routes can have different names
@app.route('/index')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run() 
