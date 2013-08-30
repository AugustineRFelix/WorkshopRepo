from nose.tools import *
from Browser.SQLFileHelper import SQLFileHelper

class TestSQLFileHelper:
	@classmethod
	def setup_class(self):
		self._sQLFileHelper = SQLFileHelper()

	def testSQLFileHelperInitializationOk(self):
		sQLFileHelper = SQLFileHelper()
	def testSQLFileHelperException(self):
		eq_('', self._sQLFileHelper.getQueryFromFile('hey, pal'))
	def testSQLFileHelperTemplateAssemblyOk(self):
		ok_(self._sQLFileHelper.getQueryFromFile('UserPermissionQuery.tpl'))
	def testSQLFileHelperTemplateAssemblyError(self):
		eq_(self._sQLFileHelper.getQueryFromFile('test.tpl'), '')