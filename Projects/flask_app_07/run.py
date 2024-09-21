from app_04 import app

# Check if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server with debug mode enabled
    # Debug mode allows for automatic code reloading during development
    app.run(debug=True)
