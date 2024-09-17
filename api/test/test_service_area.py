from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import ServiceArea


class TestServiceAreaEndpoints(TestCase):
    def setUp(self):
        self.user = {'username': 'test', 'password': '123'}
        self.service_area_data = {
            "price": "78.3",
            "name": "Filipe service in Aracaju",
            "coordinates": [
                {"lat": -10.947000, "lng": -37.074000},
                {"lat": -10.947000, "lng": -37.060000},
                {"lat": -10.933000, "lng": -37.060000},
                {"lat": -10.933000, "lng": -37.074000},
                {"lat": -10.947000, "lng": -37.074000}
            ],
            "provider": {
                "email": "filipe@email.com",
                "name": "Filipe provider in Aracaju",
                "phone_number": "799999999",
                "language": "PT",
                "currency": "REAL"
            }
        }
        self.api_client = APIClient()

        self.api_client.post(reverse('user-list'), self.user)
        response = self.api_client.post(reverse('token'), self.user, format='json')
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_create_service_area(self):
        """
            Create a service area
        """
        response = self.api_client.post(reverse('service-area-list'), self.service_area_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if service area object was added in database
        self.assertEqual(response.data['id'], ServiceArea.objects.get(id=response.data['id']).id)

    def test_retrieve_service_area(self):
        """
            Retrieve an service area
        """
        response_post = self.api_client.post(reverse('service-area-list'), self.service_area_data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        response_get = self.api_client.get(
            reverse('service-area-detail', args=[response_post.data['id']]), format='json')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_get.data['id'], response_post.data['id'])

    def test_update_servicea_area(self):
        """
            Entire update of an service area
        """
        service_area_data_updated = {
            "price": "78.3",
            "name": "Filipe service in Aracaju updated",
            "coordinates": [
                {"lat": -10.947000, "lng": -37.074000},
                {"lat": -10.947000, "lng": -37.060000},
                {"lat": -10.933000, "lng": -37.060000},
                {"lat": -10.933000, "lng": -37.074000},
                {"lat": -10.947000, "lng": -37.074000}
            ],
            "provider": {
                "email": "filipe2@email.com",
                "name": "Filipe provider in Aracaju updated",
                "phone_number": "799999999",
                "language": "PT",
                "currency": "REAL"
            }
        }

        response_post = self.api_client.post(reverse('service-area-list'), self.service_area_data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        response_put = self.api_client.put(
            reverse('service-area-detail', args=[int(response_post.data['id'])]),
            service_area_data_updated,
            format='json'
        )
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)
        self.assertEqual(response_put.data['id'], ServiceArea.objects.get(id=response_put.data['id']).id)

    def test_partial_update_service_area(self):
        """
            Partial update of an service area
        """
        service_area_data_updated = {
            "price": "199.99",
            "name": "Filipe service in Aracaju updated partially",
        }

        response_post = self.api_client.post(reverse('service-area-list'), self.service_area_data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        response_put = self.api_client.patch(
            reverse('service-area-detail', args=[int(response_post.data['id'])]),
            service_area_data_updated,
            format='json'
        )
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)
        self.assertEqual(response_put.data['id'], ServiceArea.objects.get(id=response_put.data['id']).id)

    def test_delete_service_area(self):
        """
            Delete an service area
        """
        response_post = self.api_client.post(reverse('service-area-list'), self.service_area_data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        response_delete = self.api_client.delete(
            reverse('service-area-detail', args=[response_post.data['id']]),
            format='json'
        )
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(ServiceArea.DoesNotExist):
            ServiceArea.objects.get(id=response_post.data['id'])

    def test_get_polygons(self):
        response = self.api_client.post(reverse('service-area-list'), self.service_area_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_get = self.api_client.get(
            reverse('service-area-avaiable'),
            {'lat': -10.940000, 'lng': -37.067000},
            format='json'
        )
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_get.data[0]['provider']['name'], self.service_area_data['provider']['name'])

    def test_without_authentication_on_service_area(self):
        """
            Test fail on creation of a service area without authentication
        """
        self.api_client.logout()
        response = self.api_client.post(
            reverse('service-area-list'), self.service_area_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_get_polygons_without_authentication(self):
        """
            Test fail on try to get polygons without authentication
        """
        response = self.api_client.post(reverse('service-area-list'), self.service_area_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.api_client.logout()

        response_get = self.api_client.get(
            reverse('service-area-avaiable'),
            {'lat': -10.940000, 'lng': -37.067000},
            format='json'
        )
        self.assertEqual(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_polygons_with_wrong_params(self):
        """
            Test fail on try to get polygons with wrong params
        """
        response = self.api_client.post(reverse('service-area-list'), self.service_area_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_get = self.api_client.get(
            reverse('service-area-avaiable'),
            {'x': -10.940000, 'y': -37.067000},
            format='json'
        )
        self.assertEqual(response_get.status_code, status.HTTP_400_BAD_REQUEST)
