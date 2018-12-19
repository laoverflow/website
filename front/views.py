from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from django.conf import settings
import random

def index(request):
	from random import shuffle
	x = [i for i in range(int(cache.get("total_members_load", 0)))]
	random.shuffle(x)

	members = {}
	cont = 1
	if x is not None:
		for row in x[0:60]:
			members[cont]= cache.get("member_{}".format(row))
			cont = cont + 1
		
	context = {'members': members, "lema": "Nos vemos el 26 de Diciembre en el siguiente Trivial que organizaremos en Meetup"}
	return render(request, 'index.html', context)

def get_meetup_members(request):
	import meetup.api
	client = meetup.api.Client(settings.MEETUP_APIKEY)
	group_info = client.GetGroup({'urlname': settings.MEETUP_NAME})
	group_members = client.GetMembers({'urlname': settings.MEETUP_NAME, 'group_id':group_info.id})
	cont = 0
	for row in group_members.results:
		if row.get("photo"):
			cache.set("member_{}".format(cont), {"name": row.get("name"), "photo": row.get("photo").get("thumb_link"), "link": row.get("link")}, 7200)
			cont = cont + 1

	cache.set("total_members_load", cont, 7200)
	cache.set("total_members", group_info.members, 7200)

	return render(request, 'index.html', None)

