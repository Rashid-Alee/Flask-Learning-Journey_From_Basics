# Import the Flask class from the Flask library
from flask import Flask

# Create a new Flask application instance and store it in the 'app' variable
app = Flask(__name__)


# Define a route for the root URL ('/') using the '@app.route' decorator
# This means when a user visits the base URL of the application,
# the 'hello_world' function will be executed
@app.route("/")
def hello_world():
    # Define a function named 'hello_world' that returns the string "Hello, World!"
    return "Hello, World!"


# Check if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server with debug mode enabled
    # Debug mode allows for automatic code reloading during development
    app.run(debug=True)
