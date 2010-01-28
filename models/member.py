from google.appengine.ext import db

class Member(db.Model):
  name = db.StringProperty(required=True)
  title = db.StringProperty()
  user = db.UserProperty(required=True) 
# scotches = reference from scotches.py
# comments = reference from comments.py