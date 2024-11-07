import random
import string
from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)


url_mapping = {}


def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({"error": "No URL provided"}), 400

  
    short_code = generate_short_code()

   
    url_mapping[short_code] = original_url

    shortened_url = f"http://127.0.0.1:5000/{short_code}"

    return jsonify({"shortened_url": shortened_url}), 201


@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
   
    original_url = url_mapping.get(short_code)

    if original_url:
       
        return redirect(original_url)
    else:
        
        return jsonify({"error": "Shortened URL not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)