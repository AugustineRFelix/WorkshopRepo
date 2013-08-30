import Cache
import HTTPCall

def _getInfo(hashFileName, httpCall, *httpParas):
	result = Cache.getCache(hashFileName)
	
	if result == '':
		result = httpCall(*httpParas)
		Cache.writeCache(hashFileName, result)
		
	return result

def getUserPermission(url, domainId):
	return _getInfo('%s.json' % hash(url + domainId), HTTPCall.UserPermission, url, domainId)
		
# print getUserPermission('', r'SA4SP\administrator')