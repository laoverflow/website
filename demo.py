import meetup.api
client = meetup.api.Client("6f6d2f84572e5e1f3c782d7031224e")
group_info = client.GetGroup({'urlname': 'La-Pena-Overflow'})
group_members = client.GetMembers({'urlname': 'La-Pena-Overflow', 'group_id':group_info.id})
for row in group_members.results:
	if row.get("photo"):
		print(row.get("name"), row.get("photo").get("highres_link"))

# None/None (None seconds remaining)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "/home/develop/venv/laoverflow/lib/python3.5/site-packages/meetup/api.py", line 164, in _call
#     raise exceptions.HttpNotFoundError
# meetup.exceptions.HttpNotFoundError
# >>> group_info = client.GetGroup({'urlname': 'La-Pena-Overflow'})
# 29/30 (10 seconds remaining)
# >>> group_info.name
# 'La Peña Overflow'
# >>> group_info.members
# 86