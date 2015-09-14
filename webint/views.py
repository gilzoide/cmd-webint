from flask import render_template, request, redirect, url_for, g, flash, jsonify
from flask.ext.login import login_required, login_user, logout_user, current_user
from webint import app, db, login_manager, bcrypt
from webint.models import User, Text, categories
from webint.forms import UserRegistrationForm, LoginForm
from markdown import markdown
import datetime


@app.route('/')
@app.route('/index.htm')
@app.route('/index.html')
def index():
    if current_user.is_authenticated():
        return redirect(url_for('analyze'))
    
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

        login_user(user)
        
        flash('Registration successfull. You can log in now. Thank you!', 'success')

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
            login_user(user)
            # flash('Login successfull. Welcome!', 'success')
            return redirect(url_for('analyze'))
        else:
            flash('Credentials invalid. Please try again.', 'danger')
            return redirect(url_for('index'))
    return render_template('index.html', form=form, login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/analyze')
@login_required
def analyze():
    return render_template('analyze.html', template_name="analyze")


@app.route('/submit', methods=['POST'])
@login_required
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
    current_user.texts.append(t)
    db.session.add(t)
    db.session.commit()

    return redirect(url_for('analyze'))


@app.route('/metrics/<int:text_id>.<string:fmt>')
@login_required
def metrics(text_id, fmt):
    """TODO: Docstring for metrics.

    :arg1: TODO
    :returns: TODO

    """
    text = Text.query.filter(Text.id == text_id).first()

    if fmt == 'html':
        return render_template('textinfo.html', text=text, categories=categories,
                               getattr=getattr)
    else:
        return jsonify({'error': 'Unknown format.'}) 


@app.route('/help')
@app.route('/help.htm')
@app.route('/help.html')
@login_required
def help():
    return render_template('help.html', template_name="help",
                            categories=categories)


@login_manager.user_loader
def load_user(id):
    return db.session.query(User).get(int(id))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('index'))


@app.template_filter()
def desc_to_html(string):
    lines = string.split('\n')

    if lines[0] == '' or lines[0].isspace():
        del lines[0]

    spaces = len(lines[0]) - len(lines[0].lstrip())

    string = '\n'.join(line[spaces:] for line in lines)
    return markdown(string)
