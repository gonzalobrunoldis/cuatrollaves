from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, 
                static_folder='../static',
                template_folder='../templates')
    
    CORS(app)
    
    # Import routes
    from app.routes import main
    app.register_blueprint(main)
    
    return app 