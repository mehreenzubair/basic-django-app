from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import connection
from django.db.models import Avg

from siteApp.models import Site, SiteDataEntry




def index(request):
	sites_list = Site.objects.all()
	template = loader.get_template('sites/index.html')
	context = {
		'sites_list': sites_list,
	}
	return HttpResponse(template.render(context,request))


def detail(request, site_id):
	site = Site.objects.get(pk=site_id)
	template = loader.get_template('sites/details.html')
	context = {
		'site': site,
	}
	return HttpResponse(template.render(context,request))

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def summary(request):
	template = loader.get_template('sites/summary.html')

	with connection.cursor() as cursor:
		cursor.execute("SELECT 'siteapp_site'.'site_name', SUM('siteapp_sitedataentry'.'A_value') AS 'A_value' ,SUM('siteapp_sitedataentry'.'B_value') AS 'B_value' FROM 'siteapp_sitedataentry' INNER JOIN 'siteapp_site' ON ('siteapp_sitedataentry'.'site_id_id' = 'siteapp_site'.'id') GROUP BY 'siteapp_site'.'site_name'")
		result = dictfetchall(cursor)
		context = {
		 	'result': result,
		 }

		return HttpResponse(template.render(context,request))   

def summaryAverage(request):
	template = loader.get_template('sites/average.html')
	average_data = SiteDataEntry.objects.values('site_id').annotate(Avg('A_value')).annotate(Avg('B_value'))
	average_data = list(average_data)
	for site in Site.objects.all():
		average_data[site.id-1]['site_name'] = site.site_name	
	context = {
		'average_data': average_data,
	}
	return HttpResponse(template.render(context,request)) 
