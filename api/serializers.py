from rest_framework import serializers
from django.contrib.auth.models import User


    
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)    
    
class QuestSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=256)
    master = UserSerializer()
