import httplib
import urllib
import urllib2

def UserPermission(url, domainId):
	paras = urllib.urlencode({'url':url, 'domainId':domainId})
	response = urllib.urlopen('http://127.0.0.1:8080/queryUserPermission', paras)
	return response.read()