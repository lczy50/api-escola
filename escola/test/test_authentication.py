from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usario = User.objects.create_superuser(username = 'admin', password = 'admin')
        self.url = reverse('Estudantes-list')
    
    def test_autenticacao_de_user_com_credencias_corretas(self):
        '''Teste de autenticacao de user com as credencias corretas'''
        usuario = authenticate(username = 'admin', password = 'admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_de_user_com_username_incorreta(self):
        '''Teste que verifica a autenticação de username incorreto'''
        usuario = authenticate(username = 'amin', password = 'admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
    
    def test_autenticacao_de_user_com_senha_incorreta(self):
        '''Teste que verifica a autenticação de username incorreto'''
        usuario = authenticate(username = 'admin', password = 'dmin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get_autorizada(self):
        '''teste que verifica uma requisicao get autorizada'''
        self.client.force_authenticate(self.usario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_get_nao_autorizada(self):
        '''teste que verifica uma requisicao get não autorizada'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)