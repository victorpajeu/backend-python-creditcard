import json
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .factories import CreditCardFactory

class CreditCardViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.credit_card = CreditCardFactory()

        response = self.client.post('/auth/token/', {'username': 'testuser', 'password': 'testpassword'})

        self.access_token = response.data['access']

    def test_get_credit_card_authenticated(self):
        response = self.client.get(f'/api/v1/credit-card/{self.credit_card.id}/',
                                   headers={'Content-Type': 'application/json',
                                            'Authorization': f'Bearer {self.access_token}'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['holder'], self.credit_card.holder)

    def test_list_credit_cards_authenticated(self):
        response = self.client.get('/api/v1/credit-card/',
                                   headers={'Content-Type': 'application/json',
                                            'Authorization': f'Bearer {self.access_token}'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_credit_card_unauthenticated(self):
        response = self.client.get(f'/api/v1/credit-card/{self.credit_card.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_credit_card_authenticated(self):
        new_credit_card_data = {
            'holder': 'Create User',
            'number': '5493580466552555',
            'cvv': 789,
            'exp_date': '02/2030'
        }
        response = self.client.post('/api/v1/credit-card/',
                                    data=json.dumps(new_credit_card_data),
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_credit_card_data['holder'], response.data['holder'])
        self.assertEqual(new_credit_card_data['number'], response.data['number'])
        self.assertEqual(new_credit_card_data['cvv'], response.data['cvv'])
        self.assertEqual(new_credit_card_data['exp_date'], response.data['exp_date'])
