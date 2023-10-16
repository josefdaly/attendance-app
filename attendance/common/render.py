import json

from django import http


def response(content, status=200, content_type="text/html"):
    return http.HttpResponse(content, status=status, content_type=content_type)

def json_response(content, status=200):
    return response(json.dumps(content), status=status, content_type='application/json')
