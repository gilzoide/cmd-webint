from flask import render_template, request, redirect, url_for, json, g
from webint import app, db
from webint.models import Text, find_category
import datetime


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    return 'You tried to register: ' + str(request.form)


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
