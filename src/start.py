import os
import sys
import cherrypy

from app.main import SmartHomeApp


if __name__ == '__main__':

    conf = {
        "/": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.abspath(
                os.path.join(os.path.dirname(__file__), "app/static")),
            "tools.staticdir.index": "index.html"
        }
    }
    cherrypy.quickstart(SmartHomeApp(), "/", conf)
    sys.exit(0)
