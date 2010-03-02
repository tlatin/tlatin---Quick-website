import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from google.appengine.api import users

class IndexController(webapp.RequestHandler):

  def get(self):
    template_values = {
        'login_url': users.create_login_url(self.request.uri)
      }
    
    path = os.path.join(os.path.dirname(__file__), '..', 'views', 'index.html')
    self.response.out.write(template.render(path, template_values))