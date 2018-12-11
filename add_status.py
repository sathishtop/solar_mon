#!/usr/bin/env python
import json
from datetime import datetime
import requests,time
ENERGY_FEED_URL = "http://localhost/emoncms/feed/fetch.json?ids=65,40,63,64,57"
data = {}
PV_OUTPUT_URL_TEMPLATE = "https://pvoutput.org/service/r2/addstatus.jsp?key=<API_KEY>" \
                         "&sid=63571&d={}&t={}&v1={}&v2={}&v3={}&v4={}&c1=1"
def add_status():
    date = datetime.today().strftime('%Y%m%d')
    current_time = datetime.today().strftime('%H:%M')
    request = requests.get(ENERGY_FEED_URL)
    energy_data = json.loads(request.text)
    print energy_data
    energy_generated = int(energy_data[0] * 1000);
    power_generated_in_wh = energy_data[1]
    # Consumed = generated + imported - exported
    energy_consumed = int(energy_data[0] * 1000) + int(energy_data[2] * 1000) - int(energy_data[3] * 1000)
    power_consumed = power_generated_in_wh + energy_data[4];
    PV_OUTPUT_URL = PV_OUTPUT_URL_TEMPLATE.format(date, current_time, energy_generated, power_generated_in_wh, energy_consumed,
                                                  power_consumed)
    print energy_data
    r = requests.get(PV_OUTPUT_URL)
    print r
    if r.status_code != requests.codes.ok:
        time.sleep(3)
    else:
        return
if __name__ == '__main__':
    add_status()
