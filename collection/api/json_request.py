import sys
from urllib.request import Request, urlopen
from datetime import *
import json


def json_request(url='', encoding='utf-8', success=None):
    try:
        request = Request(url)
        resp = urlopen(request)

        resp_body = resp.read().decode(encoding)
        json_result = json.loads(resp_body)

        print(json_result, type(json_result))

    except Exception as e:
        print('%s : %s' % (e, datetime.now()), file=sys.stderr)