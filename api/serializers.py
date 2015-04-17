from django.contrib.auth.models import User

from rest_framework import serializers

from django.db.models import Avg
from pinkflamingo.models import Book, Publisher, Author, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'groups',)


class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField('get_average')

    class Meta:
        model = Book
        fields = ('pk', 'title', 'description', 'isbn', 'authors', 'publisher', 'description','average_rating')

    def get_average(self, obj):
        rating = Rating.objects.filter(book=obj).aggregate(Avg('rating'))
        if rating['rating__avg'] is None:
            return "No ratings yet"
        return rating['rating__avg'] 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('pk', 'name',)


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('pk', 'name',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating', 'user', 'book',)