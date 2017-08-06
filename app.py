#!flask/bin/python
from flask import Flask, jsonify
from api_reader import *
from async_api_reader import *
from flask_cors import CORS
import datetime
import time
app = Flask(__name__)


@app.route('/weather/<path:user_address>', methods=['GET'])
def get_weather(user_address):
    user_address = url_compresss(user_address)
    geo_parameters = {'user_address':user_address,
                      'secret_key':map_api}

    #getting location and weather
    google_result = api_reader(url_map['geo'],**geo_parameters)
    city = google_result['results'][0]['address_components'][0]['short_name']                  
    location = google_result['results'][0]['geometry']['location']   

    a = time.time()
    weather_parameters = {'longitude':str(location['lng']),
                          'latitude':str(location['lat']),
                          'secret_key':weather_api}
    weather = api_reader(url_map['weather'],**weather_parameters )
    
    #gettting historic weather parameters
    historic_weather = list()
    for i in range(1,8):
      weather_parameters['time'] = (datetime.datetime.now()-datetime.timedelta(days=i)).strftime('%s')
      historic_weather.append(api_reader(url_map['history'],**weather_parameters )['currently'])

    print time.time() - a
    return jsonify({'weather_info':weather, 'city':city, 'history':historic_weather})

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)