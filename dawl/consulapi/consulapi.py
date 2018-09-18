
import json

def ifjson(valuse):
    try:
        json_object = json.loads(valuse)
    except ValueError:
        return False
    return True
