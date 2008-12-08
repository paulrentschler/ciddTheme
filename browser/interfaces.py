from plone.theme.interfaces import IDefaultPloneLayer
from plone.portlets.interfaces import IPortletManager
from plone.app.portlets.interfaces import IColumn

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer bound to a Skin
       Selection in portal_skins.
       If you need to register a viewlet only for the "ciddtheme"
       skin, this is the interface that must be used for the layer attribute
       in ciddtheme/browser/configure.zcml.
    """ 

class IPortletsBelowContent(IPortletManager, IColumn):
    """Marker interface forthe portlet manager below the content area.
        IColumn enables us to add all the standard portlets.
    """