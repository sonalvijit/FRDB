from flask import Flask
from models import db
from routes import login_manager, routes_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app=app)
db.init_app(app=app)

app.register_blueprint(routes_bp)

with app.app_context():
     db.create_all()

if __name__=="__main__":
     app.run("0.0.0.0", debug=True)