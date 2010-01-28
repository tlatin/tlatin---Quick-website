from google.appengine.ext import db

class Scotch(db.Model):
  name = db.StringProperty(required=True)
  age = db.IntegerProperty(required=True)
  lastTastedOn = db.DateProperty()
  owner = db.ReferenceProperty(Member, collection="scotches")
  scotchType = db.StringProperty(choices=set(["Single", "malt", "blended"]))
  # comments = reference from comments.py