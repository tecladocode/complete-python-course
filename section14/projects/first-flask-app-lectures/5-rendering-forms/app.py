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


# This route will just render another page with the form.
# HTML forms can then send data to another route... /post/create in this case.
@app.route('/post/form')
def form():
    return render_template('create.jinja2')


# This route will be arrived at looking like this:
# 127.0.0.1:5000/post/create?title=Hello&content=This%20is%20the%20post%20content.
@app.route('/post/create')
def create():
    title = request.args.get('title')  # This takes the 'Hello' from the title query string parameter
    content = request.args.get('content')  # This takes the 'This is the post content' form the content query string parameter.
    post_id = len(posts)  # This just gives us a new post_id as the number of posts currently existing (thing of it as an auto-increment).
    posts[post_id] = {'id': post_id, 'title': title, 'content': content}
    
    # Ths url_for gives us the route associated with the `post` function (defined in line 19). The route is /post/<int:post_id>
    # So we must also give it the argument it requires.
    # redirect then sends a response which tells the browser to load the other route instead of the one we're in.
    return redirect(url_for('post', post_id=post_id))


if __name__ == '__main__':
    app.run(debug=True)
