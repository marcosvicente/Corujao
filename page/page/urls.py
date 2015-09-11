"""page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




admin.autodiscover()



urlpatterns = [
                  url(r'^$', 'core.views.home', name='home'),

                  url(r'^grappelli/', include('grappelli.urls')),

                  url(r'^photologue/', include('photologue.urls')),

                  url(r'^event/(?P<slug>[\w_-]+)/$', 'core.views.event', name='event'),

                  url(r'^foto/(?P<slug>[\w_-]+)/$', 'core.views.foto', name='foto'),

                  url(r'^album/',  'core.views.album', name='album'),

                  url(r'^admin/', include(admin.site.urls)),

                  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                  url(r'^thanks/',  'core.views.thanks', name='thanks'),





              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
