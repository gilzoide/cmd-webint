from flask import render_template, request, redirect, url_for, g, flash
from webint import app, db, login_manager, bcrypt
from webint.models import User, Text, categories
from webint.forms import UserRegistrationForm, LoginForm
import datetime


@app.route('/')
@app.route('/index.htm')
@app.route('/index.html')
def index():
    login_form = LoginForm()
    form = UserRegistrationForm()
    return render_template('index.html', form=form, login_form=login_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return redirect(url_for('index'))

    login_form = LoginForm()
    form = UserRegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=bcrypt.generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()

        flash('Registration successfull. Welcome!', 'success')

        return redirect(url_for('analyze'))
    return render_template('index.html', form=form, login_form=login_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return redirect(url_for('index'))

    login_form = LoginForm(request.form)
    form = UserRegistrationForm()
    if login_form.validate_on_submit():  # XXX: complete
        user = db.session.query(User).filter_by(email=form.email.data).first()

        if bcrypt.check_password_hash(user.password, form.password.data):
            # XXX: complete
            flash('Login successfull. Welcome!', 'success')
            return redirect(url_for('analyze'))
        else:
            return "invalid login"
    return render_template('index.html', form=form, login_form=login_form)


@app.route('/analyze')
def analyze():
    g.Text = Text
    return render_template('analyze.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.form['publication_date']:
        publication_date = request.form['publication_date']
    else:
        publication_date = datetime.date.today()

    t = Text(title=request.form['title'],
             author=request.form['author'],
             source=request.form['source'],
             publication_date=publication_date,
             genre=request.form['genre'],
             content=request.form['content'])
    t.analyze()
    db.session.add(t)
    db.session.commit()

    return redirect(url_for('analyze'))


@app.route('/metrics/<int:text_id>')
def metrics(text_id):
    """TODO: Docstring for metrics.

    :arg1: TODO
    :returns: TODO

    """
    text = Text.query.filter(Text.id == text_id).first()
    return render_template('textinfo.html', text=text, categories=categories,
                           getattr=getattr)


@login_manager.user_loader
def load_user(id):
    return db.session.query(User).get(int(id))
