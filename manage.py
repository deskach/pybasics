#! /uar/bin/env python

from flask_script import Manager, prompt_bool

from thermos import app, db
from models import User

manager = Manager(app)

@manager.command
def initdb():
    ''' Initializes the database'''
    db.create_all()
    db.session.add(User(username='tolia', email="tolia@test.com"))
    db.session.add(User(username='daryna', email="daryna@gmail.com"))
    db.session.commit()

    print('Initialized the database')

@manager.command
def dropdb():
    '''Drops the database'''
    if prompt_bool("Are you sure?"):
        db.drop_all()
        print('Dropped the database')

@manager.command
def rundebug():
    '''Runs the Flask in debug mode i.e. app.run(debug=True)'''
    app.run(debug=True)

if __name__ == '__main__':
    manager.run()
