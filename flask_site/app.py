from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from markdown import markdown
from flask import Markup

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string lolol' # will update if this ever goes live
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    address = request.form['user_address'] 
    legislators = ['Bob Hall', 'Ted \'the Zodiac\' Cruz'] 
    print(legislators)    
    return render_template('results.html', legislators=legislators)

@app.route('/about')
def about():
   with open('about.md') as f: 
       content = Markup(markdown(f.read())) 
   return render_template('about.html', content=content)

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/test_form', methods=['GET', 'POST'])
def test_form():
    user_address = None
    form = MainForm()
    if form.validate_on_submit():
        session['user_address'] = form.user_address.data
        form.user_address.data = ''
        return redirect('/results')
    return render_template('test_form.html', form=form, name=user_address)

class MainForm(FlaskForm):
    user_address = StringField('Enter your address:', validators=[DataRequired()])
    submit = SubmitField('Disclose')

#### Reference
@app.route('/test', methods=['GET', 'POST'])
def test():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('test.html', form=form, name=name)

class NameForm(FlaskForm):
    action = 'results' 
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
