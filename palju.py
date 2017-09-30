import sys
import requests
import json
import urllib2

# Backend config
import config

from w1thermsensor import W1ThermSensor

temps = dict()

for sensor in W1ThermSensor.get_available_sensors():
    temp = sensor.get_temperature()
    print("Sensor %s has temperature %.2f" % (sensor.id, temp))
    try:
        log(sensor.id, temp)
    except requests.ConnectionError:
        print("No connection. Could not log temperature.")

def log(sensor_id, temp):
    payload = { 'id': sensor_id, 'temp': temp }

    req = urllib2.Request(config.ENDPOINT)
    req.add_header('Content-Type', 'application/json')
    req.add_header('x-token', config.X_TOKEN)

    response = urllib2.urlopen(req, json.dumps(payload))
