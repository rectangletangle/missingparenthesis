

from django.conf.urls.static import static
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urls = (url('^$', 'missingparenthesis.views.main'),
        url('^(?i)articles/(\d{1,10})$', 'missingparenthesis.views.article'),
        url('^(?i)about$', 'missingparenthesis.views.about'),
        url('^(?i)links$', 'missingparenthesis.views.links'),
        url('^(?i)archive$', 'missingparenthesis.views.archive'),
        url('^(?i)faq$', 'missingparenthesis.views.faq'),
        url('^(?i)contact$', 'missingparenthesis.views.contact'),
        url('^(?i)robots\.txt$', 'missingparenthesis.views.robots'),
        url('^admin/', include(admin.site.urls)))

urlpatterns = patterns('', *urls) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'missingparenthesis.views.error_403'
handler404 = 'missingparenthesis.views.error_404'
handler500 = 'missingparenthesis.views.error_500'

