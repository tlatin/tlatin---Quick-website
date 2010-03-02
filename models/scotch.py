from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms

from google.appengine.ext import db
from models.member import Member

class Scotch(db.Model):
  name = db.StringProperty(required=True)
  age = db.IntegerProperty(required=True)
  lastTastedOn = db.DateProperty()
  owner = db.ReferenceProperty(Member, collection_name='scotches')
  scotchType = db.StringProperty(choices=set(["Single", "malt", "blended"]))
  # comments = reference from comments.py
  
  def url(self):
    return '/scotch/' + str(self.key().id())
  
class ScotchForm(djangoforms.ModelForm):
    class Meta:
        model = Scotch
        exclude = ['owner']
        
