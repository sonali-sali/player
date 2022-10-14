"""importing required modules"""
from django.urls import path, include
from .views import (RegisterAPI,LoginAPI,UserView,TeamView,
                    TwitterView,PlayerView,PositionView,StateView,ClassView,CityView,CountryView,
                    OfferView,)
from rest_framework import routers
routers = routers.DefaultRouter()
routers.register('user',UserView, basename='user')
routers.register('player',PlayerView, basename='player')
routers.register('team',TeamView, basename='team')
routers.register('twitter',TeamView, basename='twitter')
routers.register('position',PositionView, basename='position')
routers.register('state',StateView, basename='state')
routers.register('class',ClassView, basename='class')
routers.register('city',CityView, basename='city')
routers.register('country',CountryView, basename='country')
routers.register('offer',OfferView, basename='offer')


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(routers.urls)),
    ]
