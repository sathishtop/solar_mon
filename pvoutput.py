#!/usr/bin/env python
import json
from datetime import datetime
import requests, time
import emoncms_updater

HISTORY_URL = "http://localhost/emoncms/input/post.json?node=10&apikey=c8152987954de00d0b4e07e35c765679&json="
ENERGY_FEED_URL = "http://localhost/emoncms/feed/fetch.json?ids=59,52,53,62,61,60"
data = {}
PV_OUTPUT_URL_TEMPLATE = "https://pvoutput.org/service/r2/addoutput.jsp?key=2e7416cd761ffc1770997a0b379c71757bd11364&sid=62846&d={}&g={}&e={}&io={}"

def update_pvoutput():
    attempt = 0
    while(attempt < 5):
        request = requests.get(ENERGY_FEED_URL)
        energy_data = json.loads(request.text)
        print energy_data


        energy_generated = int((energy_data[0] - energy_data[3]) * 1000)
        energy_exported  = int((energy_data[1] - energy_data[4]) * 1000)
        energy_imported  = int((energy_data[2] - energy_data[5]) * 1000)
       
       # energy_consumed = int(energy_data[3] * 1000)
        gY = energy_data[0]
        iY = energy_data[1]
        eY = energy_data[2]
        cY = get_consumed_pwer(energy_generated,energy_imported,energy_exported)

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
            emoncms_updater.do_update(iY,eY,cY,gY)
            break


def get_consumed_pwer(generated, imported, exported):
    return imported+generated-exported

if __name__ == '__main__':
    update_pvoutput()
