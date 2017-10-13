import json
import re

def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read()
    jsondata = json.loads(json_string)

    data = ''
    for item in jsondata:
        value = item.get(key)
        if value is None:
            continue

        data = ' '.join((data, re.sub(r'[^\w]', '', value)))

    return data
