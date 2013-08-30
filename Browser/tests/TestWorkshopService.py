from nose.tools import *
from WorkshopService import WorkshopService

class TestWorkshopService:
	@classmethod
	def setup_class(self):
		self._workshopService = WorkshopService()

	def testWorkshopServiceOk(self):
		ok_(self._workshopService.queryUserPermission('', 'SA4SP\\administrator'))
	def testWorkshopServiceCorrect(self):
		eq_('[{"url": "SubSite1", "permission": "Design", "title": "SubSite1"}]', self._workshopService.queryUserPermission('SubSite1', 'SA4SP\\administrator'))