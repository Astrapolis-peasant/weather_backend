import grequests
from api_reader import url_map
import datetime
import json

def get_urls(**parameters):
	#get url for current weather
	urls = list()
	url = url_map['weather']
	for key,value in parameters.iteritems():
		url = url.replace(key, value)
	urls.append(url)

	url = url_map['history']
	for i in range(1,8):
		parameters['time'] = (datetime.datetime.now()-datetime.timedelta(days=i)).strftime('%s')
		for key,value in parameters.iteritems():
			url = url.replace(key, value)
		urls.append(url)
	return urls

# def handle_response(response,**kwargs):
# 	try:
# 		json_response = json.loads(response.content)
# 		if len(json_response['daily']) == 1:
# 			result['history'] = result.get('history',list())
# 			result['history'].append(json_response['currently'])
# 		else:
# 			result['currently'] = json_response
# 	except:
# 		print 'result',type(result)


def async_requests(**parameters):
	requests = (grequests.get(u) for u in get_urls(**parameters))
	result = grequests.map(requests)
	return result
