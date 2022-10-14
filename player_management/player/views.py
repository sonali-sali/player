from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer,LoginSerializer,TwitterSerializer,TeamSerializer,InterestSerializer,RegisterSerializer,CountrySerializer,ClassSerializer,CitySerializer,HighschoolSerializer,PlayerSerializer,PositionSerializer,StateSerializer,OfferSerializer
from django.contrib.auth import login
from .models import Team,State,City,Interest,Player,Position,Class,Country,HighSchool,Offer,Twitter
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets


class RegisterAPI(generics.GenericAPIView):
    """Register API"""
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]})


class LoginAPI(generics.GenericAPIView):
    """User Login API"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)
        return Response({
            'user_id': user.pk,
            "token": AuthToken.objects.create(user)[1],})


class UserView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing User Details """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing Team Details """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CityView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing City Details """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StateView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing State Details """
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CountryView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing User Details """
    queryset = State.objects.all()
    serializer_class = CountrySerializer


class HighschoolView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing Highschool Details """
    queryset = HighSchool.objects.all()
    serializer_class = HighschoolSerializer


class ClassView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing Class Details """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class OfferView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing Offer Details """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class PositionView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing Position Details """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class InterestView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing Interest Details """
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer



class TwitterView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing Twitter Details """
    queryset = Twitter.objects.all()
    serializer_class = TwitterSerializer


class PlayerView(viewsets.ModelViewSet):
    """ A simple ViewSet for viewing and editing player Details """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

