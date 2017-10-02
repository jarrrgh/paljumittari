import sys
import requests
import json
import urllib2

# Backend config
import config

from w1thermsensor import W1ThermSensor

LOG_URL = config.ENDPOINT + '/sensor/{}/measurement?apikey={}'

def log(sensor_id, temp):
    payload = { 'value': temp }

    req = urllib2.Request(LOG_URL.format(sensor_id, config.APIKEY))
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, json.dumps(payload))

temps = dict()

for sensor in W1ThermSensor.get_available_sensors():
    temp = sensor.get_temperature()
    print("Sensor %s has temperature %.2f" % (sensor.id, temp))
    try:
        log(sensor.id, temp)
    except requests.ConnectionError:
        print("No connection. Could not log temperature.")

