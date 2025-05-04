from flask import Flask
from models import db
from routes import login_manager, routes_bp
from config import Config
from dotenv import load_dotenv
from os import getenv

load_dotenv()
port_ = getenv("PORT", 4325)

app = Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app=app)
db.init_app(app=app)

app.register_blueprint(routes_bp)

with app.app_context():
     db.create_all()

if __name__=="__main__":
     app.run(host="0.0.0.0", debug=True, port=port_)