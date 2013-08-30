from nose.tools import *

import Worker

TIME_CONSTRAINT			= 0.05

def testWorkerOk():
	ok_(Worker.getUserPermission('', r'SA4SP\administrator'))
def testWorkerQuery():
	expect = '[{"url": "", "permission": "Design", "title": "RootSite"}, {"url": "SubSite2", "permission": "Full Control", "title": "SubSite2"}, {"url": "SubSite2/SSubSite2", "permission": "View Only", "title": "SSubSite2"}, {"url": "SubSite2/SSubSite1/SSSubSite1", "permission": "Full Control", "title": "SSSubSite1"}]'
	eq_(expect, Worker.getUserPermission('', r'SA4SP\administrator'))
@timed(TIME_CONSTRAINT)
def testWorkerQueryTimeConstraint():
	Worker.getUserPermission('', r'SA4SP\administrator')
