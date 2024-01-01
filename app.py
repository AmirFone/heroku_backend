from flask import Flask
from flask_cors import CORS
from config import get_config
from routes import register_routes

app = Flask(__name__, static_url_path="")
CORS(app)
app.config.update(get_config())
register_routes(app)

if __name__ == "__main__":
    app.run()
