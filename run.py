import random
import string
from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

# In-memory dictionary to store shortened URL mappings
url_mapping = {}

# Helper function to generate random string (shortened URL code)
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Serve the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# POST /shorten - Shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({"error": "No URL provided"}), 400

    # Generate a short code for the URL
    short_code = generate_short_code()

    # Store the mapping in the dictionary
    url_mapping[short_code] = original_url

    # Construct the shortened URL
    shortened_url = f"http://127.0.0.1:5000/{short_code}"

    # Respond with the shortened URL in JSON format
    return jsonify({"shortened_url": shortened_url}), 201

# GET /{short_code} - Redirect to original URL
@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    # Check if the short code exists in the mapping
    original_url = url_mapping.get(short_code)

    if original_url:
        # Redirect to the original URL
        return redirect(original_url)
    else:
        # Return an error if the short code is not found
        return jsonify({"error": "Shortened URL not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)