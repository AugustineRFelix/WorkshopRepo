from nose.tools import *
from DatabaseEngine import DatabaseEngine

class TestDatabaseEngine:
	@classmethod
	def setup_class(self):
		self._databaseEngine = DatabaseEngine()

	def testDatabaseEngineQueryOk(self):
		ok_(self._databaseEngine.query('select * from Webs'))
	@raises(Exception)
	def testDatabaseEngineQueryException(self):
		self._databaseEngine.query('iron man')