# Import the Flask class from the Flask library
from flask import Flask, render_template, url_for

# Create a new Flask application instance and store it in the 'app' variable
app = Flask(__name__)


# Define a route for the root URL ('/') using the '@app.route' decorator
# This means when a user visits the base URL of the application,
# the 'hello_world' function will be executed
@app.route("/")
def hello_world():
    # Define a function named 'hello_world' that returns the string "Hello, World!"
    return "Hello, World!"


@app.route("/about")
def about():
    return "about me"


@app.route("/blog")
def blog():
    posts = [
        {
            "title": "Blog Post 1",
            "content": "This is the content of blog post 1",
            "author": "Rashid",
            "date_posted": "April 20, 2021",
        },
        {
            "title": "Blog Post 2",
            "content": "This is the content of blog post 2",
            "author": "Rashid",
            "date_posted": "April 21, 2021",
        },
    ]
    return render_template("blog.html", author="Rashid", posts=posts)


@app.route("/blog/<string:blog_id>")
def blog_post(blog_id):
    return f"Blog post with ID: {blog_id}"


# Check if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server with debug mode enabled
    # Debug mode allows for automatic code reloading during development
    app.run(debug=True)
