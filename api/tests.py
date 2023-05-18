from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Point
from .utils import find_closest_points, calculate_distance

class ClosestPointsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_find_closest_points_api(self):
        url = reverse('find_closest_points_api')
        data = {'points': '2,2;-1,30;20,11;4,5'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['closest_points'], '2,2;4,5')

    def test_get_points_api(self):
        point = Point.objects.create(coordinates='2,2;-1,30;20,11;4,5', closest_points='2,2;4,5')
        url = reverse('get_points_api', args=[point.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['coordinates'], '2,2;-1,30;20,11;4,5')
        self.assertEqual(response.data['closest_points'], '2,2;4,5')

    def test_find_closest_points(self):
        points = '2,2;-1,30;20,11;4,5'
        closest_points = find_closest_points(points)
        self.assertEqual(closest_points, '2,2;4,5')

    def test_calculate_distance(self):
        point1 = (2, 2)
        point2 = (4, 5)
        distance = calculate_distance(point1, point2)
        self.assertEqual(distance, 3.605551275463989)
