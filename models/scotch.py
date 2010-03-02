from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms

from google.appengine.ext import db

class Scotch(db.Model):
  name = db.StringProperty(required=True)
  age = db.IntegerProperty(required=True)
  lastTastedOn = db.DateProperty()
  owner = db.ReferenceProperty(Member, collection="scotches")
  scotchType = db.StringProperty(choices=set(["Single", "malt", "blended"]))
  # comments = reference from comments.py
  
class ItemForm(djangoforms.ModelForm):
    class Meta:
        model = Scotch
        exclude = ['added_by']