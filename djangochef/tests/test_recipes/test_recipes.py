import unittest
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APITestCase
import hashlib

from djangochef.api.seeds.ChefFactory import ChefFactory

from djangochef.Models.Chef import Chef
from djangochef.api.seeds.RecipeFactory import RecipeFactory

faker = Factory.create()


class RecipesViewsAPITestCase(APITestCase):
    def setUp(self):
        self.super_secret_password = hashlib.sha256().hexdigest()
        self.chef = ChefFactory(password=self.super_secret_password)
        self.recipe = RecipeFactory(chef_id=self.chef.id)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.test_get_token())

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

    def test_recipe_create(self):
        url = reverse('chef_recipe_create')
        data = {
            'title': self.recipe.title,
            'content': self.recipe.content,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.recipe_data = response.data

    def test_recipe_update(self):
        url = reverse('chef_recipe_edit', kwargs={'pk': self.recipe.id})
        data = {
            'title': self.recipe.title,
            'content': self.recipe.content,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.recipe_data = response.data

    def test_recipe_get(self):
        url = reverse('recip_get', kwargs={'pk':  self.recipe.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recipe_filter(self):

        url = reverse('recip_filter')
        response = self.client.get(url+"?data="+self.recipe.title, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recipe_list_by_chef(self):
        url = reverse('recip_list_chef', kwargs={'pk': self.chef.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recipe_delete(self):
        url = reverse('chef_recipe_edit', kwargs={'pk': self.recipe.id})
        response = self.client.delete(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()
