from flask import Flask

from .config import app_config
from .models import db, bcrypt
from flask_sqlalchemy import SQLAlchemy

from .views.UserView import user_api as user_blueprint
from .views.BlogpostView import blogpost_api as blogpost_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    bcrypt.init_app(app)  # add this line
    db.init_app(app)  # add this line

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogpost')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your part 2 endpoint is working'

    return app