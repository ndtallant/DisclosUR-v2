'''
    app.py
    ------

'''
from flask import Flask, render_template, url_for, session, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        session['user_state'] = form.user_state.data
        session['user_district'] = form.user_district.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form
            , user_state=session.get('user_state')
            , user_district=session.get('user_district'))

@app.route('/about')
def about():
    return render_template('about.html')

class InputForm(FlaskForm):
    user_state = SelectField(choices=[('tx', 'Texas'), ('ak', 'Alaska')])
    user_district = StringField()
