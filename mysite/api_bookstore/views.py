# Create your views here.
from rest_framework import viewsets
from .serializers import userSerializer, AuthorSerializer, BookSerializer  # serializadores
from .models import Author, Book  # modelo de datos personalizado
from django.contrib.auth.models import User # modelo de datos de usuarios

class userViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer