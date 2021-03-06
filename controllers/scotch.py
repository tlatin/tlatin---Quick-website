import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models.scotch import ScotchForm
from models.scotch import Scotch
from models.member import Member
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users


class ScotchController(webapp.RequestHandler):

  def get(self, url_data):    
      if url_data:
          if '/new' == url_data:
              self.new_form({})
          elif '/edit' == url_data[-5:]:
              event = Event.get_by_id(int(url_data[1:-5]))
              self.edit(event)
          else:
              self.show(url_data[1:])
      else:
          self.list()
  def post(self, url_data):
    if url_data:
      if '/new' == url_data:
        self.create_scotch({})
      elif '/edit' == url_data[-5:]:
        event = Event.get_by_id(int(url_data[1:-5]))
        self.edit(event)
      else:
        pass
        #Need to add what to do here
    else:
      pass
      #Also need to add something here



  def new_form(self, params):
    template_values = {
      'scotch_form' : ScotchForm(),
      'user' : users.get_current_user()
    }
    
    path = os.path.join(os.path.dirname(__file__), '..', 'views', 'scotch_new.html')
    self.response.out.write(template.render(path, template_values))
    
  def show(self, id):
    current_user = users.get_current_user()
    scotch = Scotch.get_by_id(int(id))
    if not scotch:
      self.redirect('/')
      return

    template_values = {
      'scotch' : scotch
    }

    path = os.path.join(os.path.dirname(__file__), '..', 'views', 'scotch_home.html')
    self.response.out.write(template.render(path, template_values))
  
  def create_scotch(self, params):
    data = ScotchForm(data=self.request.POST)
    if data.is_valid() and users.get_current_user():
      # Save the data, and redirect to the view page
      scotch = data.save(commit=False)
      scotch.owner = Member.gql('where user=:user', user=users.get_current_user()).get()
      scotch.put()
      self.redirect(scotch.url())
      return
    else:
      # Reprint the form
      template_values = {
        'scotch_form' : data
      }

      path = os.path.join(os.path.dirname(__file__), '..', 'views', 'scotch_new.html')
      self.response.out.write(template.render(path, template_values))
      
  def list(self):
    template_values = {
      'scotches' : Scotch.all()
    }
    
    path = os.path.join(os.path.dirname(__file__), '..', 'views', 'scotch_list.html')
    self.response.out.write(template.render(path, template_values))