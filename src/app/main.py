import cherrypy


class SmartHomeApp(object):

    @cherrypy.expose
    def test(self, **params):
        # for tests
        # /test?param=value
        return "<BR>".join(["'%s' : '%s'" % (k, v) for k, v in params.items()])
