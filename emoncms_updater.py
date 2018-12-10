#!/usr/bin/env python
import json
from datetime import datetime
import requests, time
import argparse


HISTORY_URL = "http://localhost/emoncms/input/post.json?node=10&apikey=c8152987954de00d0b4e07e35c765679&json="
data = {}

def do_update(iY,eY,cY,gY):
    data["impYesterday"] = iY 
    data["expYesterday"] = eY
    data["consumedYesterday"] = cY 
    data["generatedYesterday"] = gY 
    updated_url = HISTORY_URL + json.dumps(data)
    print updated_url
    r = requests.get(updated_url)
    print r
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--importedYesterday", "-iY", help="Energy Imported Yesterday ")
    parser.add_argument("--exportedYesterday", "-eY", help="Energy Exported Yesterday ")
    parser.add_argument("--consumedYesterday", "-cY", help="Energy Consumed Yesterday ")
    parser.add_argument("--generatedYesterday", "-gY", help="Energy Consumed Yesterday ")
    args = parser.parse_args()
    do_update(args.importedYesterday, args.exportedYesterday,args.consumedYesterday,args.generatedYesterday)
