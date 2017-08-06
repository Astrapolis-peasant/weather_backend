import urllib2
import json
from os import environ

map_api = environ.get('map_api')
weather_api = environ.get('weather_api')

url_map = {
	"geo": "https://maps.googleapis.com/maps/api/geocode/json?address=user_address&key=secret_key",
	"weather":"https://api.darksky.net/forecast/secret_key/latitude,longitude",
	"history":"https://api.darksky.net/forecast/secret_key/latitude,longitude,time"
}


def api_reader(url,**parameters):
	try:
		for key,value in parameters.iteritems():
			url = url.replace(key, value)
		print url
		response = urllib2.urlopen(url)
		json_response = json.load(response)
	except:
		print "feteching failed"
		json_response = None
	return json_response

#compress the url, so google api can read it
def url_compresss(url):
    unquote = urllib2.unquote(url)
    compressed = ''
    for i in unquote:
        if i == ' ':
            i = '+'
        compressed += i
    return compressed