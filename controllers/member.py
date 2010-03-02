import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models.member import MemberForm
from models.member import Member
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users


class MemberController(webapp.RequestHandler):

  # GET
  @login_required
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
      'member_form' : MemberForm(),
      'user' : users.get_current_user()
    }
    
    path = os.path.join(os.path.dirname(__file__), '..', 'views', 'member_new.html')
    self.response.out.write(template.render(path, template_values))
    
  def post(self, url_data):
    if url_data:
      if '/new' == url_data:
        self.create_member({})
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
        
  def create_member(self, params):
    data = MemberForm(data=self.request.POST)
    if data.is_valid():
      # Save the data, and redirect to the view page
      member = data.save(commit=False)
      member.user = users.get_current_user()
      member.put()
      self.redirect('/')
    else:
      # Reprint the form
      template_values = {
        'member_form' : data
      }

      path = os.path.join(os.path.dirname(__file__), '..', 'views', 'member_new.html')
      self.response.out.write(template.render(path, template_values))