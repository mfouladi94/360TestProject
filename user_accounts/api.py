from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.views import APIView

from user_accounts.models import UserProfile
from user_accounts.serializers import UserProfileSerializer
from utils import apiResponses
from utils.apiResponses import APIResponse


@csrf_exempt
def signup(request):
    try:
        ref_code = request.GET.get('ref')
        referrer = None

        if ref_code:
            try:
                referrer = UserProfile.objects.get(referral_code=ref_code)
            except UserProfile.DoesNotExist:
                referrer = None

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                UserProfile.objects.create(user=user)

                login(request, user)
                return apiResponses.APIResponse(status=apiResponses.OK, code=apiResponses.CODE_SUCCESS,
                                                messages="Registered Successfully")

            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])

            return apiResponses.APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed,
                                            messages=error_string)

        return apiResponses.APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed,
                                        messages="Not allowed Method")
    except Exception as e:
        return apiResponses.APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed,
                                        messages="Error in registration")


class ProfileApi(APIView):


    def get(self, request):
        try:

            if request.method == 'GET':
                userprofile = UserProfile.objects.get(user=request.user)
                serializer = UserProfileSerializer(userprofile)

                return apiResponses.APIResponse(status=apiResponses.OK, code=apiResponses.CODE_SUCCESS,
                                                messages="success", data=serializer.data)

            return apiResponses.APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed,
                                            messages="Not allowed Method")
        except Exception as e:
            print(e)
            return apiResponses.APIResponse(status=apiResponses.NOK, code=apiResponses.CODE_Failed,
                                            messages="Error in fetching profile")
