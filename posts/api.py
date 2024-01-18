from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from utils.apiResponses import *

from .models import *
from .serializers import *
from .services.post_services import *


@api_view(['GET'])
def post_list(request, page=1):
    user = request.user

    try:
        posts_list = post_list_service(user, page)
    except Exception as e:
        return APIResponse(status=NOK, messages=str(e.args))

    return APIResponse(status=OK, data=posts_list)


@api_view(['POST'])
def rate_post(request):
    user = request.user

    serializer = RateRegisterSerializer(data=request.data)

    if not serializer.is_valid():
        return APIResponse(status=NOK, messages=serializer.errors)

    data = serializer.data

    try:
        posts_list = rate_a_post_service(user, data)
    except Exception as e:
        return APIResponse(status=NOK, messages=str(e.args))

    return APIResponse(status=OK, data=posts_list)
