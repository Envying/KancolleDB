from flask import Flask, render_template, request
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
nav = Nav(app)

# registers the "top" menubar
nav.register_element('navbar', Navbar(
    'thenav',
    View('Home', 'homepage'),
    View('Form', 'form')
))


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
