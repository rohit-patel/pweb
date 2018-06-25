from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(('main.urls', 'main'), namespace='main')),
]

if settings.DEBUG:
    urlpatterns += [
        # Testing 404 and 500 error pages
        url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),
        url(r'^500/$', TemplateView.as_view(template_name='500.html'), name='500'),
    ]

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
