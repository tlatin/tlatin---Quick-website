import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class IndexController(webapp.RequestHandler):

  def get(self):
    template_values = {
      'message' : 'cocksucker! wu, i sure am glad i taught you that word',
      }
    
    path = os.path.join(os.path.dirname(__file__), '..', 'views', 'index.html')
    self.response.out.write(template.render(path, template_values))