from django.shortcuts import render, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            u, c = User.objects.get_or_create(username=request.POST['username'], email=request.POST['email'])
            if c == True:
                u.set_password(request.POST['password'])
                u.save()
                return JsonResponse({'result': 'registered'})
            else:
                return JsonResponse({'result': 'already'})
        

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def access(request):
    return JsonResponse({'result': 'granted'})