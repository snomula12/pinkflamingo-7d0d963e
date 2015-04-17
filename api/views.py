from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest_framework.views import APIView

from api.serializers import UserSerializer, BookSerializer, PublisherSerializer, AuthorSerializer, RatingSerializer
from pinkflamingo.models import Book, Publisher, Author, Rating


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer



class BooKForAuthorViewSet(APIView):
    """
    API endpoint that shows all books for a particular author.
    """
    def get(self, request, author_id, format=None):
        author = get_object_or_404(Author,pk=author_id)
        queryset = Book.objects.filter(authors=author)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class RateBookViewSet(generics.ListCreateAPIView):
    """
    API endpoint to rate books.
    """

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer



    

