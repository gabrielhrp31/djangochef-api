import unittest
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APITestCase
import hashlib

from djangochef.api.seeds.ChefFactory import ChefFactory

from djangochef.Models.Chef import Chef

faker = Factory.create()


class AuthenticationViewsAPITestCase(APITestCase):
    def setUp(self):
        self.super_secret_password = hashlib.sha256().hexdigest()
        self.chef = ChefFactory(password=self.super_secret_password)
        self.token = self.test_get_token()

    def test_get_token(self):
        url = reverse('login')
        data = {
            'email': self.chef.email,
            'password': self.super_secret_password,
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']
        return token

    def test_chef_register(self):
        url = reverse('chef')
        data = {
            'email':faker.email(),
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
            'age': faker.random_int(),
            'restaurant_name': faker.company(),
            'password': faker.password(),
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_chef_auth(self):
        url = reverse('login')
        data = {
            'email': self.chef.email,
            'password': self.super_secret_password,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_refresh(self):
        url = reverse('token_refresh')
        data = {
            'token': self.token
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()
