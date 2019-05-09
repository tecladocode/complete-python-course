from flask import Flask


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


# This route expects to be in the format of /post/0 (for example).
# Then it will pass 0 as argument to the post() function.
@app.route('/post/<int:post_id>')
def post(post_id):
    """
    This function runs when a user visits route such as:

    - /post/0
    - /post/2
    - /post/99

    But not:

    - /post/a
    - /post/something/else
    - /posts/1

    Then we get the 0 as a number (not a string!) as argument, so we can use it.
    """
    post = posts.get(post_id)  # Retrieve the post from our global posts dictionary by the ID passed in as argument.
    return f"Post {post['title']}, content:\n\n{post['content']}"  # Return the title and content formatted a bit nicer.


if __name__ == '__main__':
    app.run(debug=True)
