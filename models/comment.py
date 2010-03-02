from google.appengine.ext import db

from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms

from models.member import Member
from models.scotch import Scotch

class Comment(db.Model):
  text = db.StringProperty()
  liked = db.StringProperty(choices=set(["liked", "ambivalent", "disliked"]))
  preferred = db.BooleanProperty()
  member = db.ReferenceProperty(Member, collection_name="comments")
  scotch = db.ReferenceProperty(Scotch, collection_name="comments")
  
class CommentForm(djangoforms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['member', 'scotch']
    