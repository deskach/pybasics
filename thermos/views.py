from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

from forms import BookmarkForm, LoginForm, SignupForm
from models import User, Bookmark
from thermos import app, db, login_manager


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title="Thermos",
                           new_bookmarks=Bookmark.new_bookmarks(5)
                           )


@app.route('/user/<username>')  # hsere <username> becomes a parameter for the function
def user(username):
    usr = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=usr)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usr = User.get_by_username(username=form.username.data)
        if usr is not None and usr.verify_password(form.password.data):
            login_user(usr, form.remember_me.data)
            flash("Logged in successfully as {}.".format(usr.username))
            return redirect(request.args.get('next') or url_for('user', username=usr.username))
        flash('Incorrect username or password.')
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        usr = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(usr)
        db.session.commit()
        flash('Welcome, {}! Please login.'.format(usr.username))
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(user=current_user, url=url, description=description)
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
