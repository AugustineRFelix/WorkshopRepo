import os

from DatabaseEngine import DatabaseEngine
from nose.tools import *

TIME_CONSTRAINT = 0.05

class TestSQL:
	def setup(self):
		self._databaseEngine = DatabaseEngine()

	def user_permission_query(self):
		vardeclaration = 'declare @url as varchar(256);set @url = \'\';declare @user as varchar(256);set @user = \'SA4SP\\administrator\';declare @siteid as varchar(40);select @siteid = SiteId from Webs where FullUrl=@url;'
		userPrincipalIdSelection = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'UserPrincipalIdSelection.sql'))).read()
		return vardeclaration + userPrincipalIdSelection
	def test_user_selection(self):
		expect = 1
		records = self._databaseEngine.query(self.user_permission_query())
		eq_(expect, records[0][0])
	@timed(TIME_CONSTRAINT)
	def test_user_selection_time_constraint(self):
		self._databaseEngine.query(self.user_permission_query())

	def roles_info_selection_query(self):
		vardeclaration = 'declare @url as varchar(256);set @url = \'\';declare @user as varchar(256);set @user = \'SA4SP\\administrator\';declare @siteid as varchar(40);select @siteid = SiteId from Webs where FullUrl=@url;'
		rolesInfoSelection = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'RolesInfoSelection.sql'))).read()
		return vardeclaration + rolesInfoSelection
	def test_roles_info_selection(self):
		expects = [
			(1073741825, u'Limited Access'), 
			(1073741826, u'Read'), 
			(1073741827, u'Contribute'), 
			(1073741828, u'Design'), 
			(1073741829, u'Full Control'), 
			(1073741924, u'View Only')
		]
		records = self._databaseEngine.query(self.roles_info_selection_query())
		eq_(expects, records)
		# for n in range(len(expects)):
			# eq_(expects[n][0], records[n][0])
			# eq_(expects[n][1], records[n][1])
	@timed(TIME_CONSTRAINT)
	def test_rolse_info_selection_time_constraint(self):
		records = self._databaseEngine.query(self.roles_info_selection_query())

	def unique_ancestor_web_content_query(self):
		vardeclaration = 'declare @url as varchar(256);set @url = \'\';'
		uniqueAncestorWebContentSelection = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'UniqueAncestorWebContentSelection.sql'))).read()
		return vardeclaration + uniqueAncestorWebContentSelection
	def test_unique_ancestor_web_content(self):
		expect = ('18BAE6AC-57EF-46E9-8290-40ABBB3D25D8', '', 'RootSite', '7CE3ADC2-A300-43C9-BC78-1A0F84C44087')
		records = self._databaseEngine.query(self.unique_ancestor_web_content_query())
		eq_(expect, records[0])
	@timed(TIME_CONSTRAINT)
	def test_unique_ancestor_web_content_time_constraint(self):
		records = self._databaseEngine.query(self.unique_ancestor_web_content_query())
		
	def unique_children_web_content_query(self):
		vardeclaration = 'declare @url as varchar(256);set @url = \'\';declare @siteid as varchar(40);declare @urllike as varchar(256);set @urllike = dbo.fn_EscapeForLike(@url, 1);select @siteid = SiteId from Webs where FullUrl=@url;'
		uniqueChildrenWebContentSelection = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'uniqueChildrenWebContentSelection.sql'))).read()
		return vardeclaration + uniqueChildrenWebContentSelection
	def test_unique_children_web_content(self):
		expects = [
			('9777079F-AD4E-42E9-BCCC-3D07BD9AE3A8','SubSite2/SSubSite1/SSSubSite1','SSSubSite1','8E8A260C-BB32-4315-822A-B02A715179F4'),
			('E29E47BF-F27E-4074-962A-65E8DC6394D6','SubSite2','SubSite2','C9DB8626-7191-4B4E-A30E-A67C07451F67'),
			('DDC8DB34-4588-4764-A749-6A57299B89FE','SubSite2/SSubSite2','SSubSite2','070C444D-A822-4A7C-8B2A-A6D81B170E12')
		]
		records = self._databaseEngine.query(self.unique_children_web_content_query())
		eq_(expects, records)
	@timed(TIME_CONSTRAINT)
	def test_unique_children_web_content_time_constraint(self):
		records = self._databaseEngine.query(self.unique_children_web_content_query())