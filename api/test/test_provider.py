from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Provider


class TestProviderEndpoints(TestCase):
    def setUp(self):
        self.user = {'username': 'test', 'password': '123'}
        self.provider_data = {
            "email": "filipe@email.com",
            "name": "Filipe Provider",
            "phone_number": "799999999",
            "language": "PT",
            "currency": "REAL"
        }
        self.api_client = APIClient()

        self.api_client.post(reverse('user-list'), self.user)
        response = self.api_client.post(reverse('token'), self.user, format='json')
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_create_provider(self):
        """
            Create an provider
        """
        email = self.provider_data['email']
        response = self.api_client.post(
            reverse('provider-list'), self.provider_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if provider object was added in database
        self.assertEqual(email, Provider.objects.get(email=email).email)

    def test_retrieve_provider(self):
        """
            Retrieve an provider
        """
        response_post = self.api_client.post(
            reverse('provider-list'), self.provider_data, format='json'
        )
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        response_get = self.api_client.get(reverse('provider-detail', args=[response_post.data['id']]), format='json')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_get.data['id'], response_post.data['id'])

    def test_update_provider(self):
        """
            Entire update of an provider
        """
        provider_data_updated = {
            "email": "filipe2@email.com",
            "name": "Filipe Provider 2",
            "phone_number": "799999999",
            "language": "EN",
            "currency": "USD"
        }

        response_post = self.api_client.post(reverse('provider-list'), self.provider_data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        response_put = self.api_client.put(
            reverse('provider-detail', args=[int(response_post.data['id'])]),
            provider_data_updated,
            format='json')
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)
        self.assertEqual(response_put.data['email'], Provider.objects.get(email=provider_data_updated['email']).email)

    def test_partial_update_provider(self):
        """
            Partial update of an provider
        """
        provider_data_updated = {
            "email": "filipe3@email.com",
        }

        response_post = self.api_client.post(reverse('provider-list'), self.provider_data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        response_patch = self.api_client.patch(
            reverse('provider-detail', args=[response_post.data['id']]),
            provider_data_updated,
            format='json')
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response_patch.data['email'],
            Provider.objects.get(email=provider_data_updated['email']).email)

    def test_delete_provider(self):
        """
            Delete an provider
        """
        response_post = self.api_client.post(reverse('provider-list'), self.provider_data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        response_delete = self.api_client.delete(
            reverse('provider-detail', args=[response_post.data['id']]),
            format='json')
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Provider.DoesNotExist):
            Provider.objects.get(email=response_post.data['email'])
    
    def test_without_authentication_on_provider(self):
        """
            Test fail on creation of a provider without authentication
        """
        self.api_client.logout()
        response = self.api_client.post(
            reverse('provider-list'), self.provider_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
