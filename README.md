# jokes_api
A simple REST API on Python to generate and manage strange jokes
### Use:
* Create User: POST api/v1/users
* Login: POST api/v1/users/login
* Get Me: GET api/v1/users/me 
* Edit Me: PUT api/v1/users/me
* Get all users: GET api/v1/users 
* DELETE account: api/v1/users/me 
* Generate a joke: POST api/v1/jokes 
* Get all my jokes: GET api/v1/jokes 
* Get a joke: GET api/v1/jokes/<int:joke_id> 
* Update a joke: PUT api/v1/jokes/<int:joke_id> 
* Delete a joke: DELETE api/v1/jokes/<int:joke_id>

### Installation:
Install Python, Pipenv, Postgres
```sh
$ git clone https://github.com/alissiawells/jokes_api.git
$ cd /jokes_api
$ pipenv shell
$ pipenv install
$ export FLASK_ENV=development
$ export DATABASE_URL=postgres://name:password@houst:port/jokes_api_db
$ export JWT_SECRET_KEY=verysecretkey
$ python run.py
```

Test the api using Postman or curl: https://jokesapi.herokuapp.com/
