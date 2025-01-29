import os
from flask import Flask
from flask_cors import CORS

def create_app():
    # Ensure Flask finds the correct paths
    app = Flask(
        __name__,
        static_folder=os.path.abspath("static"),    # Fix static folder path
        template_folder=os.path.abspath("templates")  # Fix templates folder path
    )
    
    CORS(app)
    
    # Import routes
    from app.routes import main
    app.register_blueprint(main)
    
    return app
