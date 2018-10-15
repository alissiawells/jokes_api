#/src/views/JokeView.py
import requests
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.JokeModel import JokeModel, JokeSchema

joke_api = Blueprint('joke_api', __name__)
joke_schema = JokeSchema()


@joke_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Joke Function
  """
  req_data = request.get_json()
  res = requests.get('https://geek-jokes.sameerkumar.website/api')
  if res.ok:
    req_data['contents'] = res.json()
  req_data['owner_id'] = g.user.get('id')
  data, error = joke_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  post = JokeModel(data)
  post.save()
  data = joke_schema.dump(post).data
  return custom_response(data, 201)

@joke_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
  """
  Get All jokes
  """
  posts = JokeModel.get_all_jokes()
  data = joke_schema.dump(posts, many=True).data
  myjokes = []
  for i in data:
    if i.get('owner_id') == g.user.get('id'):
      myjokes.append(i)
  return custom_response(myjokes, 200)

@joke_api.route('/<int:joke_id>', methods=['GET'])
@Auth.auth_required
def get_one(joke_id):
  """
  Get A joke
  """
  post = JokeModel.get_one_joke(joke_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = joke_schema.dump(post).data
  return custom_response(data, 200)

@joke_api.route('/<int:joke_id>', methods=['PUT'])
@Auth.auth_required
def update(joke_id):
  """
  Update A joke
  """
  req_data = request.get_json()
  post = JokeModel.get_one_joke(joke_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = joke_schema.dump(post).data
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)
  
  data, error = joke_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  post.update(data)
  
  data = joke_schema.dump(post).data
  return custom_response(data, 200)

@joke_api.route('/<int:joke_id>', methods=['DELETE'])
@Auth.auth_required
def delete(joke_id):
  """
  Delete A joke
  """
  post = JokeModel.get_one_joke(joke_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = joke_schema.dump(post).data
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

