from flask import Flask
from app.extensions import db, login_manager
from app.config import Config

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login_page"

    from .routes.auth_routes import auth_ka_bp
    from .routes.page_routes import page_wala_bp
    from .routes.post_routes import post_wala_bp
    from .routes.user_routes import user_wala_bp

    app.register_blueprint(auth_ka_bp)
    app.register_blueprint(page_wala_bp)
    app.register_blueprint(post_wala_bp)
    app.register_blueprint(user_wala_bp)

    return app
