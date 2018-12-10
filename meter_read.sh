#!/bin/sh
while [ 1 ]
do
	/var/solarmonj/meter_read.py
	sleep 10
done
