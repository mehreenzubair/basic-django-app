from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<site_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'summary/$', views.summary, name='summary'),
    url(r'summary-average/$', views.summaryAverage, name='summaryAverage'),
]