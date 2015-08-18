from unittest import TestCase
from django.contrib.auth.models import User
import requests
from rest_framework.authtoken.models import Token
import json
from api.models import Quest

from rest_framework.test import APIClient
# Create your tests here.
class ApiTestCase(TestCase):
    
    def setUp(self):
        global token
        global c
        
        u, c = User.objects.get_or_create(username='user1', email='user@test.com')
        u.set_password('password')
        u.save()
        token, created = Token.objects.get_or_create(user=u)
        
        c = APIClient()
         
         
    def test_check_quest(self):

        c.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        payload = {'quest_name':'Primera mision', 'description':'Completa esta mision' }
        response = c.post('/api/v1/quest/create/', data=payload)

        payload = {'quest_name':'Segunda mision', 'description':'Completa esta mision' }
        response = c.post('/api/v1/quest/create/', data=payload)
        
        response = c.get('/api/v1/quest/')
        j = json.loads(response.content)
        self.assertTrue(j[0]['name'] == 'Primera mision')
        self.assertTrue(j[1]['name'] == 'Segunda mision')
         
    def test_create_quest(self):
        
        # GET method
        response = c.get('/api/v1/quest/create/')
        self.assertTrue(response.content == '{"detail":"Authentication credentials were not provided."}')
        
        # Fail to create quest
        payload = {'quest_name':'Primera mision', 'description':'Completa esta mision'}
        response = c.post('/api/v1/quest/create/', data=payload)
        self.assertTrue(response.content == '{"detail":"Authentication credentials were not provided."}')
        
        # Success when create quest 
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        payload = {'quest_name':'Primera mision', 'description':'Completa esta mision' }
        response = c.post('/api/v1/quest/create/', data=payload)
        self.assertEquals(Quest.objects.get(pk=1).name, 'Primera mision')
        self.assertEquals(Quest.objects.get(pk=1).master.username, 'user1')
        self.assertTrue(response.content == '{"result": "success"}')
        
        
    def test_register_view(self):
        
        # Register an user
        payload = {'username':'newuser', 'email':'newuser@test.com', 'password':'pass'}
        response = c.post('/api/v1/register/', data=payload)
        self.assertTrue(response.content == '{"result": "registered"}')
        
        # Register it again
        
        response = c.post('/api/v1/register/', data=payload)
        self.assertTrue(response.content == '{"result": "already"}')
        
        
    def test_access_view(self):
        
        # Can not access
        response = c.get('/api/v1/access/')
        self.assertTrue(response.content == '{"detail":"Authentication credentials were not provided."}')
        
        # Can access
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = c.get('/api/v1/access/')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.content == '{"result": "granted"}')
        
    def test_login_url(self):
        # False credentials
        response = c.post('/api/v1/login/', data={'username':'1234', 'password':'1234'})
        self.assertTrue(response.status_code == 400)
        self.assertTrue(response.content == '{"non_field_errors":["Unable to log in with provided credentials."]}')
        
        # True credentials # STATUS CODE = 200
        response = c.post('/api/v1/login/', data={'username':'user1', 'password':'password'})
        j = json.loads(response.content)
        self.assertTrue(j['token'] == token.key)
        
        # No POST data
        response = c.post('/api/v1/login/')
        self.assertTrue(response.status_code == 400)
        self.assertTrue(response.content == '{"username":["This field is required."],"password":["This field is required."]}')
    