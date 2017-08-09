from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^summary$', views.summary_sum, name='summary_sum_page'),
    url(r'^summary-average$', views.summary_avg, name='summary_avg_page'),
]