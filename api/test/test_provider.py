from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Provider


class APITest(TestCase):
    def setUp(self):
        self.provider_data = {
            "email": "filipe@email.com",
            "name": "Filipe Provider",
            "phone_number": "799999999",
            "language": "PT",
            "currency": "REAL"
        }
        self.api_client = APIClient()
    
    def test_create_provider(self):
        """
            Create a provider
        """
        email = self.provider_data['email']
        response = self.client.post(
            reverse('provider'), self.provider_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #Check if provider object was added in database
        self.assertEqual(email, Provider.objects.get(email=email).email)
    
    def test_retrive_provider(self):
        """
            Retrieve a provider
        """
        response_create = self.client.post(
            reverse('provider'), self.provider_data, format='json'
        )
        reverse_retrieve = self.client.get(
            reverse('provider'), self.provider_data, format='json'
        )