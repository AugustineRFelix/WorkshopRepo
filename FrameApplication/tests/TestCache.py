from nose.tools import *

import os
import Cache

class TestCache:
	@classmethod
	def setup_class(self):
		self._tempReadFile = os.path.abspath(os.path.join(Cache.CACHE_FOLDER_PATH, 'tempRead'))
		self._tempWriteFile = os.path.abspath(os.path.join(Cache.CACHE_FOLDER_PATH, 'tempWrite'))
		with open(self._tempReadFile, 'w') as file:
			file.write('hey, pal')

	@classmethod
	def teardown_class(self):
		os.remove(self._tempReadFile)
		os.remove(self._tempWriteFile)
		
	def testGetCacheOK(self):
		ok_(Cache.getCache('tempRead'))
	def testWriteCacheOK(self):
		Cache.writeCache('tempWrite', 'hey, dude')
		with open(self._tempWriteFile) as file:
			eq_('hey, dude', file.read())