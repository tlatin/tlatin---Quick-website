import os
import wsgiref.handlers
import cgi, logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


from controllers.main import MainHandler

def main():
  application = webapp.WSGIApplication(
       [('/', MainHandler)],
       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
