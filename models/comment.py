from google.appengine.ext import db

class Comment(db.Model):
  text = db.StringProperty()
  liked = db.StringProperty(choices=set(["liked", "ambivalent", "disliked"]))
  preferred = db.BooleanProperty()
  member = db.ReferenceProperty(Member collection="comments")
  scotch = db.ReferenceProperty(Scotch collection="comments")