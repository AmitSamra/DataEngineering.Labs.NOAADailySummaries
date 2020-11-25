import urllib.request
import urllib.parse
import json
import os
import json
import pandas as pd
from dotenv import load_dotenv
dotenv_local_path = './.env'
load_dotenv(dotenv_path=dotenv_local_path, verbose=True)


file_counter = 0
offset_counter = 1

while file_counter < 2:

	headers = {'token':os.environ.get('NOAA_Token')}

	myurl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-12-01&enddate=2018-12-31&limit=1000&' + 'offset=' + str(offset_counter)
	request = urllib.request.Request(myurl, headers = headers)
	file_path = './data/daily_summaries/daily_summaries_dec_2018_'+str(file_counter)+'.json'

	with urllib.request.urlopen(request) as f:
		data = json.load(f)

		with open(file_path, 'w') as g:
			json.dump(data,g)

	file_counter += 1
	offset_counter += 1000

