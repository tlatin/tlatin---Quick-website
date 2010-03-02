import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from google.appengine.api import users
from models.member import Member

class IndexController(webapp.RequestHandler):

  def get(self):
    member = None
    if users.get_current_user():
      member = Member.gql('where user=:user', user=users.get_current_user()).get()

    template_values = {
        # 'login_url': users.create_login_url(self.request.uri),
        'login_url': '/members/new',
        'member': member
      }
    
    path = os.path.join(os.path.dirname(__file__), '..', 'views', 'index.html')
    self.response.out.write(template.render(path, template_values))