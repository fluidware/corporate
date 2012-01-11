from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'corporate.views.index', {}, 'index'),
	(r'^frontpage/$', 'corporate.views.frontpage', {}, 'frontpage'),
	#(r'^about/$', 'corporate.views.about', {}, 'about'),
	(r'^contact/$', 'corporate.views.contact', {}, 'contact'),
)

from django.conf import settings

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	) 