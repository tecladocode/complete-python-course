from flask import Flask, render_template, request, redirect, url_for


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
    if not post:
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
    return render_template('post.jinja2', post=post)


# This route will be arrived at looking like this:
# 127.0.0.1:5000/post/create, but with either:
# - POST and including the form data; or
# - the user may load this page with the browser—which is always using GET.
@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':  # if the method is 'POST' we know the form sent us to this page, so there is data to process.
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post', post_id=post_id))
    # if we are here it means we did not redirect to the post; so we must've loaded this using a GET.
    # the browser always sends GET, so this means the user wants to load the page (as opposed to giving us data via the form).
    # We can render the form.
    return render_template('create.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
