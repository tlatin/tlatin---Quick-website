import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class MemberController(webapp.RequestHandler):

  # GET
  def get(self, url_data):    
      if url_data:
          if '/new' == url_data:
              self.new({})
          elif '/search' == url_data:
              params = self.parameterize() 
              self.search(params)
          elif '/edit' == url_data[-5:]:
              event = Event.get_by_id(int(url_data[1:-5]))
              self.edit(event)
          else:
              self.show(url_data[1:])
      else:
          self.list()
          
  def new(self, params):
    template_values = {

    }
    
    path = os.path.join(os.path.dirname(__file__), '..', 'views', 'member_new.html')
    self.response.out.write(template.render(path, template_values))