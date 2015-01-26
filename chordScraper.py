import requests
import simplejson
import jsonpickle

with open('top100s.json', 'r') as f:
	data = simplejson.load(f)

for song in data['songs']:
	url = "http://tabs.ultimate-guitar.com/%s/%s/%s_crd.htm" % (song['artist'][0].lower(), song['artist'].replace(" ", "_"), song['title'].replace(" ", "_"))
	r = requests.get(url)

	if r.status_code == 200:
		song['chord_url'] = url
	else:
		song['chord_url'] = ""

jsonpickle.set_encoder_options('simplejson', indent=4)
frozen = jsonpickle.encode(data)

with open('top100s.json', 'w') as f:
	f.write(frozen)
