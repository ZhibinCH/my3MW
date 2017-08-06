from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^summary$', views.py_summary_sum, name='summary_sum_page'),
    url(r'^summary-average$', views.py_summary_avg, name='summary_avg_page'),
]