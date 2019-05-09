from flask import Flask

# We create a new Flask app with a unique name (normally we use '__main__' since that's always unique across all files imported in the project).
app = Flask(__name__)


# This decorator registers the '/' route with our app.
# When a user visits the '/' route (which is the homepage), the home() function will execute.
@app.route('/')
def home():
    """
    This function will run when the user visits the '/' route (the homepage).
    It just returns 'Hello, world!' as any good first application should!
    """
    return 'Hello, world!'


# Only run the code inside the if statement if we've execute this file.
# We don't want to run our app if we have imported this file, as running the app
# would block and prevent importing this file, since it runs until the app is shut down.
if __name__ == '__main__':
    # Run the app.
    # The debug=True flag is just here for development purposes.
    # It gives us more information if an error happens.
    app.run(debug=True)