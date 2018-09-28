import os
from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)

def gen_connection_string():
    # if not on Google then use local MySQL
    if not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        return 'mysql://root@localhost/admin'
    else:
        conn_name = os.environ.get('CLOUDSQL_CONNECTION_NAME' '')
        sql_user = os.environ.get('CLOUDSQL_USER', 'root')
        sql_pass = os.environ.get('CLOUDSQL_PASSWORD', '')
        conn_template = 'mysql+mysqldb://%s:%s@/admin?unix_socket=/cloudsql/%s'
        return conn_template % (sql_user, sql_pass, conn_name)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = gen_connection_string()
db = SQLAlchemy(app)

# SQLAchemy model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Unicode(80), nullable=False)
    title = db.Column(db.Unicode(255), nullable=False)
    body = db.Column(db.UnicodeText())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title

# Marshmallow serialization schema
class PostSerializer(Schema):
    id = fields.Integer()
    author = fields.Str()
    title = fields.Str()
    body = fields.Str()
    created_at = fields.DateTime()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/world_maps')
def world_maps():
    return render_template('world_maps.html')

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

@app.route('/posts')
def get_posts():
    # Fetch all the posts
    posts = Post.query.all()
    # Create a serialization schema
    schema = PostSerializer(many=True)
    # Return all posts as json
    return jsonify({ 'items': schema.dump(posts).data })

def bootstrap_db():
    # Create db tables if they don't exits. NOT SAFE FOR PRODUCTION USE!
    db.create_all()
    # create a couple of posts if there are none
    if Post.query.count() == 0:
        p1 = Post(author=u'john',
                title=u'Do you know your Latin?',
                body=u'Lorem ipsum dolor sit amet',
                created_at=datetime.utcnow() + timedelta(days=-1))
        p2 = Post(author=u'mary',
                title=u'Easy way to a better life',
                body=u'Eat healthy, move more, lift heavy, laugh.')
        db.session.add_all([p1, p2])
        db.session.commit()

bootstrap_db()

if __name__ == '__main__':
    app.run(debug=True)
