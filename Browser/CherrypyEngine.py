import cherrypy
import threading

class CherrypyServer(threading.Thread):
	@property
	def ServerStarted(self):
		return cherrypy.engine.state == cherrypy.process.wspbus.states.STARTED
		
	@property
	def ServerStopped(self):
		return cherrypy.engine.state == cherrypy.process.wspbus.states.STOPPED

	def __init__(self, suppressScreenPrinting = False):
		threading.Thread.__init__(self)
		self.sync = threading.Condition()
		if suppressScreenPrinting:
			cherrypy.config.update({'log.screen': False})

	def run(self, service):
		with self.sync:
			cherrypy.server.socket_port = 8080
			cherrypy.tree.mount(service, '/')
			cherrypy.engine.start()
		# cherrypy.engine.block()

	def stop(self):
		with self.sync:
			cherrypy.engine.exit()
			cherrypy.server.stop()