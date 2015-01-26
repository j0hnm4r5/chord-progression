import requests
from bs4 import BeautifulSoup
import simplejson
import jsonpickle

data = {"songs": []}

with open('top100s_test.json', 'a') as f:
	for year in xrange(1940, 2014):
		r = requests.get("http://billboardtop100of.com/%s-2/" % year)
		soup = BeautifulSoup(r.text, 'lxml')

		for row in soup.find_all('tr'):
			i = 0
			entry = {'year' : year}
			for col in row:
				if col.name == 'td':

					text = col.text

					if i == 0:
						entry['rank'] = int(text)
					elif i == 1:
						entry['artist'] = text
					else:
						entry['title'] = text
					i += 1

			data["songs"].append(entry)

	jsonpickle.set_encoder_options('simplejson', indent=4)
	frozen = jsonpickle.encode(data)

	f.write(frozen)

