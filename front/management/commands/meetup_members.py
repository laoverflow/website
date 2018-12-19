from django.conf import settings
from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError
import datetime
import meetup.api

class Command(BaseCommand):
	help = 'Get members for Meetup API'

	def handle(self, *args, **options):		
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

