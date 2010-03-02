from google.appengine.ext import db

from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms

class Member(db.Model):
  name = db.StringProperty(required=True)
  title = db.StringProperty()
  user = db.UserProperty(required=False) 
  # scotches = reference from scotches.py
  # comments = reference from comments.py
  
  
  
class MemberForm(djangoforms.ModelForm):
      class Meta:
          model = Member
          exclude = ['user']