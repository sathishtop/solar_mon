#!/usr/bin/env python

from eastron.modbusmeter import ModbusMeter
import time
import json
import requests

MODBUS_MASTER_HOST = '192.168.43.201'
SDM220_SLAVE_ID = 1

DELAY = 10
debug=True

UPDATE_URL = 'http://localhost/emoncms/input/post.json?node=1&apikey=c8152987954de00d0b4e07e35c765679&json='

#Register configuration.
SDM220_REGS = [
        # Symbol    Reg#  Format
        ('V1',      0x00, '%6.2f'),  # Voltage Phase 1 [V]
        ('V2',      0x02, '%6.2f'),  # Voltage Phase 2 [V]
        ('V3',      0x04, '%6.2f'),  # Voltage Phase 3 [V]
        ('I1',      0x06, '%6.2f'),  # Current Phase 1 [A]
        ('I2',      0x08, '%6.2f'),  # Current Phase 2 [A]
        ('I3',      0x0A, '%6.2f'),  # Current Phase 3 [A]
        ('P1',      0x0C, '%6.0f'),  # Power Phase 1 [W]
        ('P2',      0x0E, '%6.0f'),  # Power Phase 2 [W]
        ('P3',      0x10, '%6.0f'),  # Power Phase 3 [W]
        ('P_total', 0x34, '%6.0f'),  # Total system power [W]
        ('F',       0x46, '%6.2f'),  # Line Frequency [Hz]
        ('E_imp',    0x48, '%6.2f'),  # Import energy [kWh]
        ('E_exp',    0x4a, '%6.2f')   # Export energy [kWh]
    ]

sdm220_meter = ModbusMeter(MODBUS_MASTER_HOST, SDM220_SLAVE_ID)

if __name__ == '__main__':

#    while True:
        sdm220_values = sdm220_meter.get_meter_vals(SDM220_REGS)
#        net_power_value = int(sdm220_values['P'])
#        if(net_power_value < 0):
#            sdm220_values['P_imp'] = 0
#            sdm220_values['P_exp'] = -1 * net_power_value
#        else:
#            sdm220_values['P_imp'] = net_power_value
#            sdm220_values['P_exp'] = 0

        updated_url = UPDATE_URL + json.dumps(sdm220_values)
        r = requests.get(updated_url)

        #Sleep and repeat.
 #       time.sleep(DELAY)
