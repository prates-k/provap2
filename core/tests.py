from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Produto

class ProdutoAPITestCase(APITestCase):

    def test_cadastrar_produto(self):
        url = '/api/produtos/'
        data = {
            'codigo_barras': '7891234567890',
            'nome': 'Teclado Mecânico RGB',
            'preco': 249.90,
            'quantidade_estoque': 15
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 1)
        self.assertEqual(Produto.objects.get().nome, 'Teclado Mecânico RGB')