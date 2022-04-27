#import requests

#params = {"currentRequestTimestamp":1650364352881,"contentID":"606f11ed95a53e001b54f345","type":"radio","chunkUp":False,"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1yc25vb3Bib3pAZ21haWwuY29tIiwidXNlcklEIjoiNjE0ZTBkMDRiNDM1MWQwMDI2MDFkYmEzIiwiaWF0IjoxNjUwMzY0MzE0fQ.yAG5dnY3h5UTA4KYDPIawwY4ms3NwvtHlRHysjpjHFk","socketID":"ZcyUjX9yyjPVGlkzAAN5"}
#r = requests.get('https://api.aiva.creators.aiva.ai/content/stream', params=params)

#print(r.text)





import json
from requests import requests.async

def add_option_params(args):
    options = {'rpp': 5, 'include_entities': 1, 'result_type': 'mixed'}
    args['params'].update(options)
    return args

requests = []

for search_term in ['test1', 'test2', 'test3']:
    request = async.get('http://search.twitter.com/search.json',
                        params={'q': search_term},
                        hooks={'args': add_option_params})
    requests.append(request)

for result in async.map(requests):
    print result.url, json.loads(result.text)['completed_in']