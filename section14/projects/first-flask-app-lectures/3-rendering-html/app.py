from flask import Flask, render_template


app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>')
def post(post_id):
    """
    This function renders a template from the `templates` folder in the directory of app.py.
    It will find the `post.jinja2` template and render it with the data passed in.

    Look at `post.jinja2` for information on how the variable `post` gets used there.
    """
    return render_template('post.jinja2', post=posts.get(post_id))


if __name__ == '__main__':
    app.run(debug=True)
