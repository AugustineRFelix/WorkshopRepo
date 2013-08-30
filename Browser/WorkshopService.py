import json
import cherrypy

from DatabaseEngine import DatabaseEngine
from SQLFileHelper import SQLFileHelper

class WorkshopService():
	def __init__(self):
		self._databaseEngine = DatabaseEngine()
		self._sQLFileHelper = SQLFileHelper()

	@cherrypy.expose
	def index(self):
		return ('<form action="queryUserPermission" method="post"> ' 
			'<p>URL <input type="text" name="url" value="" size="15" maxlength="40"/></p> '  
			'<p>DomainID <input type="text" name="domainID" value="" size="10" maxlength="40"/></p> ' 
			'<p><input type="submit" value="Submit"/><input type="reset" value="Clear"/></p> ' 
			'</form>')
	
	@cherrypy.expose
	def queryUserPermission(self, url, domainID):
		try:
			records = self._databaseEngine.query(self._sQLFileHelper.getQueryFromFile('UserPermissionQuery.tpl') % {'url':url, 'user':domainID})
			jsonResult = [ {'url':record.url, 'title':record.title, 'permission':record.permission} for record in records]

			return json.dumps(jsonResult)
		except:
			return ''