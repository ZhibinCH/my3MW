from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sites_overview, name='homepage'),
    url(r'^sites$', views.sites_overview, name='sites_page'),
    url(r'^sites/(?P<site_id>\w+)/$',views.site_detail,name='site_detail')
]