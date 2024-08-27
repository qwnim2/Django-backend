from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return Response({'message': f'Hello World! It is {current_time} now.'})

@api_view(['GET'])
def cat_image(request):
    try:
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        cat_image_url = response.json()[0]['url']
        return Response({'url': cat_image_url})
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)