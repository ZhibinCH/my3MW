from django.http import HttpResponse
from django.template import loader
from sites.models import *

def sites_overview(request):
    
    template = loader.get_template('sites/sites_list.html')
    context = {}
    context['sites'] = Sites.objects.all()
    return HttpResponse(template.render(context, request))


def site_detail(request,site_id):
    
    template = loader.get_template('sites/site_detail.html')
    context = {}
    site = Site.objects.filter(site_id = site_id)
    site_name = Sites.objects.get(id = site_id).name  
    context['site'] = site
    context['site_name'] = site_name
    return HttpResponse(template.render(context, request))

