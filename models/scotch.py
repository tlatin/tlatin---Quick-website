from google.appengine.ext import db

class Scotch(db.Model):
  name = db.StringProperty(required=True)
  age = db.IntegerProperty(required=True)
  lastTastedOn = db.DateProperty()
  owner = db.UserProperty()
  scotchType = db.StringProperty(choices=set(["Single", "malt", "blended"]))
