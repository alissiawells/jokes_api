# src/models/Joke.py
from . import db
import datetime
from marshmallow import fields, Schema

class JokeModel(db.Model):
  """
  Joke Model
  """

  __tablename__ = 'jokes'

  id = db.Column(db.Integer, primary_key=True)
  contents = db.Column(db.Text, unique=True, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.contents = data.get('contents')
    self.owner_id = data.get('owner_id')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_jokes():
    return JokeModel.query.all()
  
  @staticmethod
  def get_one_joke(id):
    return JokeModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class JokeSchema(Schema):
  """
  Joke Schema
  """
  id = fields.Int(dump_only=True)
  contents = fields.Str(required=False)
  owner_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
