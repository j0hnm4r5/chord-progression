import requests
from bs4 import BeautifulSoup
import json

with open('top100s.json', 'a') as f:
	for year in xrange(1959):
		r = requests.get("http://billboardtop100of.com/%s-2/" % year)
		soup = BeautifulSoup(r, 'lxml')

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
			f.write(json.dumps(entry) + '\n')
