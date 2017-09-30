import sys
import requests

from w1thermsensor import W1ThermSensor
from phant import Phant

p = Phant(jsonPath='/home/pi/palju/keys.json', fields=['id', 'temp'])

temps = dict()

for sensor in W1ThermSensor.get_available_sensors():
    temp = sensor.get_temperature()
    print("Sensor %s has temperature %.2f" % (sensor.id, temp))
    try:
        p.log(sensor.id, temp)
    except requests.ConnectionError:
        print("No connection. Could not log temperature.")
