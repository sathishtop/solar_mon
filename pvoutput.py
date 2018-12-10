#!/usr/bin/env python
import json
from datetime import datetime
import requests, time
import emoncms_updater

HISTORY_URL = "http://localhost/emoncms/input/post.json?node=10&apikey=c8152987954de00d0b4e07e35c765679&json="
ENERGY_FEED_URL = "http://localhost/emoncms/feed/fetch.json?ids=36,56,55,52,53"
data = {}
PV_OUTPUT_URL_TEMPLATE = "https://pvoutput.org/service/r2/addoutput.jsp?key=2e7416cd761ffc1770997a0b379c71757bd11364&sid=62846&d={}&g={}&e={}&io={}"

def update_pvoutput():
    attempt = 0
    while(attempt < 5):
        request = requests.get(ENERGY_FEED_URL)
        energy_data = json.loads(request.text)
        print energy_data
        energy_generated = int(energy_data[0] * 1000)
        energy_exported = int(energy_data[1] * 1000)
        energy_imported = int(energy_data[2] * 1000)
       # energy_consumed = int(energy_data[3] * 1000)
        iY = energy_data[3]
        eY = energy_data[4]
        cY = energy_data[2] + energy_data[0] - energy_data[1]

       # temperature_max = int(energy_data[5])
        date = datetime.today().strftime('%Y%m%d')
        PV_OUTPUT_URL = PV_OUTPUT_URL_TEMPLATE.format(date, energy_generated, energy_exported, energy_imported)
        print PV_OUTPUT_URL
        r = requests.get(PV_OUTPUT_URL)
        print r
        attempt += 1
        if(r.status_code != requests.codes.ok):
            time.sleep(3)
        else:
            print "Successfully uploaded the data in pvoutput, now updating emoncms"
            emoncms_updater.do_update(iY,eY,cY)
            break

if __name__ == '__main__':
    update_pvoutput()
