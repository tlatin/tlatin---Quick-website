import wsgiref.handlers
import cgi, logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


from controllers.index import IndexController
from controllers.member import MemberController
from controllers.scotch import ScotchController

def main():
  application = webapp.WSGIApplication(
       [('/', IndexController),
        ('/members(|/\d+|/new|/search|/\d+/edit)', MemberController),       
        ('/scotch(|/\d+|/new|/\d+/edit)', ScotchController),       
       ],
       
       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
