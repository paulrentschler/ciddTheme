from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets import common

class LogoViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/logo.pt')

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                            name=u'plone_portal_state')

        self.navigation_root_url = portal_state.navigation_root_url()

class SearchBoxViewlet(common.SearchBoxViewlet):
    render = ViewPageTemplateFile('templates/searchbox.pt')

class FooterViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/footer.pt')

# class CustomViewlet(ViewletBase):
#    render = ViewPageTemplateFile('templates/custom_viewlet.pt')

#    def update(self):
        # set here the values that you need to grab from the template.
        # stupid example:
        # self.stupid_display = "Yay! Wh00t!"