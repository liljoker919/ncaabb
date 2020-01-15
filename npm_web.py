import random
import string

import cherrypy


class Index(object):
    @cherrypy.expose()
    def index(self):
        return open('index.html')

    @cherrypy.expose()
    def Model(self):
        return open('model.html')
         


if __name__ == '__main__':
    cherrypy.quickstart(Index())