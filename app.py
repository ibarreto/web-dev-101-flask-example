from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

posts = [
    {'title': 'My first post', 'content': 'this is my first post! hooray!', 'slug': 'my-first-post'}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/posts/<string:slug>')
def show_post(slug):
    post = next((post for post in posts if post["slug"] == slug), None)
    if post is None:
        return render_template('not_found.html')
    return render_template('post.html', post=post)

@app.route('/posts', methods=['POST'])
def create_post():
    return redirect(url_for('index'))
