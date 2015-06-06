from flask import render_template, request, redirect, url_for, g, flash
from webint import app, db
from webint.models import Text, categories
from webint.forms import UserRegistrationForm
import datetime


@app.route('/')
@app.route('/index.html')
def index():
    form = UserRegistrationForm()
    return render_template('index.html', form=form)


@app.route('/register', methods=['POST'])
def register():
    form = UserRegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data, form.password.data)
        # db.session.add(user)
        flash('Registration successfull. Welcome!', 'success')
        return redirect(url_for('analyze'))
    return render_template('index.html', form=form)


@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('analyze'))


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
