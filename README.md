# paljumittari
Temperature logger for RPi.

## Usage
1. Add this to /boot/config.txt:

```
# Enable General Purpose I/O
dtoverlay=w1-gpio
```

2. And something like this to /var/spool/cron/crontab:

```
# Log palju temperatures once a minute
*/1 * * * * /usr/bin/python /home/pi/palju/palju.py
```
