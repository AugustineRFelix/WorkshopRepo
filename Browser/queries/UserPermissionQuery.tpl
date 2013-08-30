declare @url as varchar(256)
set @url = '%(url)s'
declare @user as varchar(256)
set @user = '%(user)s'

declare @urllike as varchar(256)
set @urllike = dbo.fn_EscapeForLike(@url, 1)
declare @siteid as varchar(40)
select @siteid = SiteId from Webs where FullUrl=@url

;with
UniqueWebContent as (
	{% include 'UniqueAncestorWebContentSelection.sql' %}
	union
	{% include 'UniqueChildrenWebContentSelection.sql' %}
),
UserPricipalId as (
	{% include 'UserPrincipalIdSelection.sql' %}
),
RolesInfo as (
	{% include 'RolesInfoSelection.sql' %}
)
select UniqueWebContent.FullUrl as url, UniqueWebContent.Title as title, RolesInfo.Title as permission from UniqueWebContent, RoleAssignment, RolesInfo where 
	UniqueWebContent.ScopeId = RoleAssignment.ScopeId and 
	RoleAssignment.PrincipalId = (select * from UserPricipalId) and 
	RolesInfo.RoleId = RoleAssignment.RoleId