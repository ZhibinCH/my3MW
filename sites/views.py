from django.shortcuts import render,render_to_response
from django.http import Http404
from sites.models import *

def sites_overview(request):
    
    if not Sites.objects.all():

         site = Sites(site_name='Demo Site', site_id='1',date='2015-02-01',a_value = '12',b_value='16')
         site.save()
         site = Sites(site_name='Demo Site', site_id='1',date='2015-02-03',a_value = '20',b_value='100')
         site.save()
         site = Sites(site_name='Demo Site', site_id='1',date='2015-02-10',a_value = '20',b_value='80')
         site.save()
         site = Sites(site_name='ABC Site', site_id='2',date='2015-02-03',a_value = '5',b_value='15')
         site.save()
         site = Sites(site_name='XYZ Site', site_id='3',date='2015-02-15',a_value = '5',b_value='15')
         site.save()
         site = Sites(site_name='XYZ Site', site_id='3',date='2015-02-28',a_value = '5',b_value='15')
         site.save()
         
    return render_to_response('sites/sites_list.html')


def site_detail(request,site_id):
    site = Sites.objects.filter(site_id = site_id)
    return render_to_response('sites/site_detail.html',{'site':site})
