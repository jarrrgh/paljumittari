# paljumittari
Temperature logger for RPi.

## Usage
1. Install requirements:

```
pip install -r requirements.pip
```

2. Add this to /boot/config.txt:

```
# Enable General Purpose I/O
dtoverlay=w1-gpio
```

3. And something like this to crontab (crontab -e):

```
# Log palju temperatures once a minute
*/1 * * * * /usr/bin/python /home/pi/paljumittari/palju.py
```

## Optional and notes-to-self
1. Disable starting desktop after boot. Desktop can be launched again with 'startx'.

```
sudo raspi-config
```

Boot Options > Desktop / CLI > Console Autologin

2. Connect to wifi automatically

```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

```
network={
    ssid="ssid"
    psk="password"
}
```

