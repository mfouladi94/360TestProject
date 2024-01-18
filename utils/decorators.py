import json
from functools import wraps
from django.http import JsonResponse

from utils import apiResponses


def transform_request_body_data(func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            try:
                # sample decorator template
                body = json.loads(request.body.decode('utf-8'))
                method = body["method"]
                new_body = body.pop('data')
                result = func(request, new_body, *args, **kwargs)
                return result

            except Exception as e:
                return apiResponses.APIResponse(status=apiResponses.NOK , code= apiResponses.CODE_Failed, messages="failed", data=e.args)

    return wrapper
