from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('cat-image/', views.cat_image, name='cat_image'),
]