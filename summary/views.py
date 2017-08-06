from django.shortcuts import render,render_to_response
from django.db.models import Avg,Sum,Max
from sites.models import *
from summary.models import *

def summary_sum(request):
    max_id = Sites.objects.all().aggregate(max_id= Max('site_id'))['max_id']
    if not SumSites.objects.all():
        for i in range(0,int(max_id)):
            site_a_sum = Sites.objects.filter(site_id = i+1).aggregate(a_sum= Sum('a_value'))['a_sum']
            site_b_sum = Sites.objects.filter(site_id = i+1).aggregate(b_sum= Sum('b_value'))['b_sum']
            site = Sites.objects.filter(site_id = i+1)
            sum_site = SumSites(site_name=site[0].site_name, site_id=i+1,a_value = site_a_sum,b_value=site_b_sum)
            sum_site.save()
    sum_sites = SumSites.objects.all()         
    return render_to_response('summary/summary_sum.html',{'summary_sites':sum_sites})
    
def summary_avg(request):
    max_id = Sites.objects.all().aggregate(max_id= Max('site_id'))['max_id']
    if not AvgSites.objects.all():
        for i in range(0,int(max_id)):
            site_a_avg = Sites.objects.filter(site_id = i+1).aggregate(a_avg= Avg('a_value'))['a_avg']
            site_b_avg = Sites.objects.filter(site_id = i+1).aggregate(b_avg= Avg('b_value'))['b_avg']
            site = Sites.objects.filter(site_id = i+1)
            avg_site = AvgSites(site_name=site[0].site_name, site_id=i+1,a_value = site_a_avg,b_value=site_b_avg)
            avg_site.save()
    avg_sites = AvgSites.objects.all()       
    return render_to_response('summary/summary_avg.html',{'summary_sites':avg_sites})
    
def py_summary_sum(request):
    sites = Sites.objects.all()
    max_id = maximum(sites)
    if not SumSites.objects.all():
        for i in range(0,max_id):
            site = Sites.objects.filter(site_id = i+1)
            sum_a,sum_b = summation(site)
            sum_site = SumSites(site_name=site[0].site_name, site_id=i+1,a_value = sum_a,b_value=sum_b)
            sum_site.save()
    sum_sites = SumSites.objects.all()  
    return render_to_response('summary/summary_sum.html',{'summary_sites':sum_sites})
    
def py_summary_avg(request):
    sites = Sites.objects.all()
    max_id = maximum(sites)
    if not AvgSites.objects.all():
        for i in range(0,int(max_id)):
            site = Sites.objects.filter(site_id = i+1)
            avg_a,avg_b = addition(site)
            avg_site = AvgSites(site_name=site[0].site_name, site_id=i+1,a_value = avg_a,b_value=avg_b)
            avg_site.save()
    avg_sites = AvgSites.objects.all()   
    return render_to_response('summary/summary_avg.html',{'summary_sites':avg_sites})

def maximum(sites):
    max_id = int(sites[0].site_id) 
    for item in sites: 
        if int(item.site_id)> max_id:
            max_id = int(item.site_id)
    return max_id
            
def summation(site):
    sum_a = 0
    sum_b = 0
    for item in site: 
        sum_a = sum_a + item.a_value
        sum_b = sum_b + item.b_value
    return sum_a,sum_b
    
def average(site):
    sum_a, sum_b = summation(site)
    return sum_a/len(site),sum_b/len(site)