from nose.tools import *

import sys
import time
import HTTPCall

sys.path.append(r'C:\Work\Python\WorkShop\Browser')
from WorkshopService import WorkshopService
from CherrypyEngine import CherrypyServer 

class TestHTTPCall:
	@classmethod
	def setup_class(self):
		self._cherrypyServer = CherrypyServer(True)
		self._cherrypyServer.run(WorkshopService())

	@classmethod
	def teardown_class(self):
		self._cherrypyServer.stop()

	def testUserPermissionCallOK(self):
		while not self._cherrypyServer.ServerStarted:
			time.sleep(2)
			
		ok_(HTTPCall.UserPermission('', r'SA4SP\administrator'))