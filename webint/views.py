from flask import render_template, request, redirect, url_for, json, g
from webint import app
from webint.models import Text, as_json, find_category


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
    Hypernyms = find_category('hypernyms')
    c = Hypernyms(hypernyms_verbs=10)

    return json.dumps([{c.__tablename__: as_json(c)}])

    t = Text(title=request.form['title'],
             author=request.form['author'],
             source=request.form['source'],
             publication_date=request.form['publication_date'],
             genre=request.form['genre'],
             content=request.form['content'])
    return '<p>'.join(t.analyze().split('\n'))
