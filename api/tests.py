from unittest import TestCase
from django.contrib.auth.models import User
import requests
from rest_framework.authtoken.models import Token
import json

from rest_framework.test import APIClient
# Create your tests here.
class ApiTestCase(TestCase):
    
    def setUp(self):
        global token
        
        u, c = User.objects.get_or_create(username='user1', email='user@test.com')
        u.set_password('password')
        u.save()
        token, created = Token.objects.get_or_create(user=u)
        
        
    def test_access_view(self):
        c = APIClient()
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = c.get('/api/v1/access/')
        self.assertTrue(response.content == 'Access granted')
    
    
    def test_login_url(self):
        
        c = APIClient()
        
        # False credentials
        response = c.post('/api/v1/login/', data={'username':'1234', 'password':'1234'})
        self.assertTrue(response.content == '{"non_field_errors":["Unable to log in with provided credentials."]}')
        
        # True credentials
        response = c.post('/api/v1/login/', data={'username':'user1', 'password':'password'})
        j = json.loads(response.content)
        self.assertTrue(j['token'] == token.key)
        
        # No POST data
        response = c.post('/api/v1/login/')
        self.assertTrue(response.content == '{"username":["This field is required."],"password":["This field is required."]}')
    