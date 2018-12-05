from flask import Flask, render_template, request
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')
'''
@app.route('/results', methods=['POST'])
def results():
    address = request.form['user_address'] 
    return render_template('results.html')

@app.route('/about')
def about():
   return render_template('about.html')
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
