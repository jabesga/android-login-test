from django.shortcuts import render, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from api.models import Quest
from api.serializers import QuestSerializers
from rest_framework.renderers import JSONRenderer

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
 
 
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def check_quest(request):
    q = Quest.objects.all()
    serializer = QuestSerializers(q, many=True)
    json = JSONRenderer().render(serializer.data)
    return HttpResponse(json)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def create_quest(request):
    if request.method == 'POST':
        q = Quest(name=request.POST['quest_name'], description=request.POST['quest_name'], master=request.user)
        q.save()
        return JsonResponse({'result': 'success'})    