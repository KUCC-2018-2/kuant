from rest_framework import viewsets

from .models import User, Message, Write, Scrap
from .serializers import UserSerializer, MessageSerializer, WriteSerializer, ScrapSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ScrapViewSet(viewsets.ModelViewSet):
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer


class WriteViewSet(viewsets.ModelViewSet):
    queryset = Write.objects.all()
    serializer_class = WriteSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

