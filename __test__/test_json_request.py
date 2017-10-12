from analysis_fb.collection.api import json_request as jr

url = 'http://192.168.1.38:8088/mysite3/api/guestbook/list'


def success_fetch_guestbook_list(response):
    pass


jr.json_request(url=url, success=success_fetch_guestbook_list)
