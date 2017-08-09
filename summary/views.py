from django.http import HttpResponse
from django.template import loader
from django.db.models import Avg
from sites.models import *
    
def summary_sum(request):
    template = loader.get_template('summary/summary.html')
    context = {}
    sites = Sites.objects.all() 
    
    for site in sites:
       site.A_value = sum([item.a_value for item in site.site_set.all()])
       site.B_value = sum([item.b_value for item in site.site_set.all()])
    context['sites'] = sites
    context['sum'] = True
    
    return HttpResponse(template.render(context, request))
    
    
def summary_avg(request):
    template = loader.get_template('summary/summary.html')
    context = {}
    sites = Sites.objects.all()
    for site in sites: 
       site.A_value = site.site_set.all().aggregate(a_avg= Avg('a_value'))['a_avg']
       site.B_value = site.site_set.all().aggregate(b_avg= Avg('b_value'))['b_avg']

    context['sites'] = sites
    context['average'] = True
        
    return HttpResponse(template.render(context, request))