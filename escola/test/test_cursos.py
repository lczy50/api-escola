from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usario = User.objects.create_superuser(username = 'admin', password = 'admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user = self.usario)
        self.curso_01 = Curso.objects.create(
            codigo = 'F010',
            descricao = 'Curso de Flask 10',
            nivel = 'B'
        )
        self.curso_02 = Curso.objects.create(
            codigo = 'F011',
            descricao = 'Curso de Flask 11',
            nivel = 'B'
        )

    def test_requisao_get_para_listar_cursos(self):
        '''Teste de requisicao GET de curso'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisao_get_para_listar_um_curso(self):
        '''Teste de requisicao GET de um curso'''
        response = self.client.get(self.url+'1/')
        dados_cursos = Curso.objects.get(pk=1)
        dados_cursos_serializado = CursoSerializer(instance=dados_cursos).data
        self.assertEqual(response.data, dados_cursos_serializado)

    def test_requisicao_post_para_criar_um_curso(self):
        '''Teste de requisicao POST de curso'''
        dados = {
            'codigo':'teste1',
            'descricao':'curso de teste',
            'nivel':'I'
        }
        response = self.client.post(self.url, data = dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_curso(self):
        '''Teste de requisicao DELETE para um curso'''
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_criar_um_curso(self):
        '''Teste de requisicao PUT para um Curso'''
        dados = {
            'codigo':'teste2',
            'descricao':'curso de teste',
            'nivel':'I'
        }
        response = self.client.put(f'{self.url}1/', data = dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    