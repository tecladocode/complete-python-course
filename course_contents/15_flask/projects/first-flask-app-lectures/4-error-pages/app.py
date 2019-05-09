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
    post = posts.get(post_id)
    # If the post was not found, then we can render a different page instead—the user will see an error page.
    if not post:
        # Here we pass another variable, the string `message`.
        # It can be used inside the jinja template.
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
    return render_template('post.jinja2', post=post)


if __name__ == '__main__':
    app.run(debug=True)
