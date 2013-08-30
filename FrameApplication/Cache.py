import os

CURRENT_FOLDER_PATH		= os.path.dirname(__file__)
CACHE_FOLDER_PATH		= os.path.join(CURRENT_FOLDER_PATH, '..', 'Cache')

def _getFilePath(function):
	def __getFilePath(fileName, *args, **kwargs):
		return function(os.path.abspath(os.path.join(CACHE_FOLDER_PATH, fileName)), *args, **kwargs)
	return __getFilePath

@_getFilePath
def getCache(fileName):
	try:
		with open(fileName) as cacheFile:
			return cacheFile.read()
	except:
		return ''

@_getFilePath			
def writeCache(fileName, content):
	with open(fileName, 'w') as cacheFile:
		cacheFile.write(content)