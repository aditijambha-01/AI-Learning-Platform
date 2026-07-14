from flask import Flask
from flask_cors import CORS
import os
from routes.api import api_bp

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
CORS(app)

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)