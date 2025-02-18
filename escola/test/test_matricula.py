from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula

class MatriculasTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usario = User.objects.get(username = 'luca')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user = self.usario)
        self.matricula_estudante = Estudante.objects.get(pk=1)
        self.matricula_curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.get(pk=1)

    def test_requisao_get_para_listar_matriculas(self):
        '''Teste de requisição de GET para matriculas'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_uma_matriculas(self):
        '''Teste de requisição de POST para matriculas'''
        dados = {
            'curso': self.matricula_curso.pk,
            'estudante': self.matricula_estudante.pk,
            'periodo':'M'
        }
        response = self.client.post(self.url, data = dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_uma_matricula(self):
        '''Teste de requisicao DELETE para uma matricula'''
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_criar_uma_matricula(self):
        '''Teste de requisicao PUT para uma matricula'''
        dados = {
            'curso': self.matricula_curso.pk,
            'estudante': self.matricula_estudante.pk,
            'periodo':'M'
        }
        response = self.client.put(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)