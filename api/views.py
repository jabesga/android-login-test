from django.shortcuts import render, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            print "ES UN POST"
            print request.data # <-------- AQUI ES ERROR QUITAR ESTA LINEA
            print request.POST['username']
    return HttpResponse("Hola")
        

@api_view(['GET'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def access(request):
    return HttpResponse("Access granted")