from flask import Flask, request

def create_app():
 
    app = Flask(__name__)

    
    @app.route('/shorten', methods=['POST'])
    def shorten_url():
       
        data = request.get_json()
        url = data.get('url')
        
        return "URL shortened successfully!"

    return app
