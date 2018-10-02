import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/world_maps')
def world_maps():
    return render_template('world_maps.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/posts')
def get_posts():
    # Fetch all the posts
    posts = Post.query.all()
    # Create a serialization schema
    schema = PostSerializer(many=True)
    # Return all posts as json
    return jsonify({ 'items': schema.dump(posts).data })


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
