# Create your views here.
import Worker

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return HttpResponse(('<form action="queryUserPermission" method="post"> '
			'<p>URL <input type="text" name="url" value="" size="15" maxlength="40"/></p> '  
			'<p>DomainID <input type="text" name="domainID" value="" size="10" maxlength="40"/></p> ' 
			'<p><input type="submit" value="Submit"/><input type="reset" value="Clear"/></p> ' 
			'</form>'))

@csrf_exempt
def queryUserPermission(request):
	url = request.POST.get('url')
	domainID = request.POST.get('domainID')
	return HttpResponse(Worker.getUserPermission(url, domainID))