import json
from django.utils.deprecation import MiddlewareMixin


class RouterMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # Router for creating single ENdpoint Api for django
        if request.method == 'POST':
            pass

    def process_response(self, request, response):
        if response.status_code == 404:
            pass
        return response
