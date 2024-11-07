from flask import Flask, request

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Define the POST route for /shorten
    @app.route('/shorten', methods=['POST'])
    def shorten_url():
        # Get the URL from the JSON request
        data = request.get_json()
        url = data.get('url')
        
        # Logic to shorten the URL (not implemented yet)
        return "URL shortened successfully!"

    return app
