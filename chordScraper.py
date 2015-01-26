import requests
import simplejson
from bs4 import BeautifulSoup
import jsonpickle

def find_chords(r):
	soup = BeautifulSoup(r.text)
	chords = []
	try:
		for chord in soup.find(class_="print-visible").next_sibling.next_sibling.find_all("span"):
			chords.append(chord.text)
	except:
		print "Can't find any chords"

	return chords

with open('top100s.json', 'r') as f:
	data = simplejson.load(f)

for song in data['songs']:
	try:
		url = "http://tabs.ultimate-guitar.com/%s/%s/%s_crd.htm" % (song['artist'][0].lower(), song['artist'].replace(" ", "_"), song['title'].replace(" ", "_"))
		r = requests.get(url)

		if r.status_code == 200:
			print url
			song['chord_url'] = url
			song['chords'] = find_chords(r)
		else:
			song['chord_url'] = ""
			song['chords'] = ""
	except:
		print "There was a problem"
		song['chord_url'] = ""
		song['chords'] = ""

jsonpickle.set_encoder_options('simplejson', indent=4)
frozen = jsonpickle.encode(data)

with open('top100s.json', 'w') as f:
	f.write(frozen)
