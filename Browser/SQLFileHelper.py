import os
from jinja2 import FileSystemLoader, Environment

CURRENT_FOLDER_PATH     = os.path.dirname(__file__)
QUERIES_FOLDER_PATH		= os.path.join(CURRENT_FOLDER_PATH, 'queries')
TEMPLATE_FOLDER_PATH	= os.path.join(QUERIES_FOLDER_PATH, 'templates')

class SQLFileHelper:
	def __init__(self):
		self._environment = Environment(loader = FileSystemLoader([QUERIES_FOLDER_PATH, TEMPLATE_FOLDER_PATH]))
		
	def getQueryFromFile(self, file_name):
		try:
			template = self._environment.get_template(file_name)
			return template.render()
		except:
			return ''