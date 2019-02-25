'''
app.py
------

Server logic lives here!

'''
from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template
from flask import url_for, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Move to env later
app.config['SECRET_KEY'] = 'my secret key'

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
    user_district = StringField() #SelectField()
