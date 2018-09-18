
import sys
import requests
import json
import base64


def add(newkey,newval):

    res = requests.get('http://192.168.1.216:8500/v1/kv/?recurse')
    jsres = json.loads(res.text)

    lengh = len(jsres)

    for i in range(lengh):
        keycon = jsres[i]['Key']
        key_new = str(keycon).replace('dianda', newkey)

        valcon = jsres[i]['Value']
        val_old = str(base64.b64decode(valcon.encode('utf-8')), 'utf-8')
        val_new = val_old.replace('diandainfo', newval)

        requests.put('http://192.168.1.216:8500/v1/kv/%s' %(key_new), val_new.encode('utf-8'))

if __name__ == "__main__":

    key = sys.argv[1]
    val = sys.argv[2]
    add(key, val)
