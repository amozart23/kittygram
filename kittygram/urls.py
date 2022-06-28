from django.urls import path

from cats.views import CatViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter() 

urlpatterns = [
    path('cats/', CatViewSet),
    path('cats/<int:pk>/', CatViewSet),
]