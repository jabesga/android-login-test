from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.authtoken.models import Token

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def home(request):

    token = Token.objects.get_or_create(user=request.user) # Authorization: Token 4070bfa4f47854f3fe7f466a7a01743f105726be
    return HttpResponse(token[0].key)
