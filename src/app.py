#src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint
from .views.JokeView import joke_api as joke_blueprint


def create_app(env_name):
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  # initializing bcrypt and db
  bcrypt.init_app(app)
  db.init_app(app)

  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
  app.register_blueprint(joke_blueprint, url_prefix='/api/v1/jokes')

  @app.route('/', methods=['GET'])
  def index():
    s = '''
Create User: POST api/v1/users <br>\n
Login: POST api/v1/users/login <br>\n
Get Me: GET api/v1/users/me <br>\n
Edit Me: PUT api/v1/users/me <br>\n
Get all users: GET api/v1/users <br>\n
DELETE account: api/v1/users/me <br>\n
Generate a joke: POST api/v1/jokes <br>\n
Get all my jokes: GET api/v1/jokes <br>\n
Get a joke: GET api/v1/jokes/<int:joke_id> <br>\n
Update a joke: PUT api/v1/jokes/<int:joke_id> <br>\n
Delete a joke: DELETE api/v1/jokes/<int:joke_id>
'''

    return s
  return app

