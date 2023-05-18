from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Point
from .utils import find_closest_points

@api_view(['POST'])
def find_closest_points_api(request):
    print(request.data)
    points = request.data.get('points')
    if points:
        closest_points = find_closest_points(points)
        point = Point.objects.create(coordinates=points, closest_points=closest_points)
        return Response({'closest_points': closest_points})
    else:
        return Response({'error': 'No points provided.'}, status=400)

@api_view(['GET'])
def get_points_api(request, point_id):
    point = get_object_or_404(Point, id=point_id)
    return Response({'coordinates': point.coordinates, 'closest_points': point.closest_points})
