from google.appengine.ext import db

class Scotch(db.Model):
    name = db.StringProperty(required=True)
    age = db.IntegerProperty(required=True)
    lastTastedOn = db.DateProperty()
    owner = db.UserProperty(required=True)
	type = db.StringProperty(choices=set(["Single", "malt", "blended"]))