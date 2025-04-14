from app import create_app
import os

# Create the Flask application
app = create_app()

if __name__ == "__main__":
    # Get the port from environment variables or default to 5000
    port = int(os.environ.get("PORT", 5000))

    # Run the app using Flask's built-in server (good for dev)
    app.run(host="0.0.0.0", port=port, debug=False)