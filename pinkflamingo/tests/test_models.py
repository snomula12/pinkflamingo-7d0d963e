# encoding: utf-8
import random
from django.contrib.auth.models import User
from django.db.models import Sum, Avg
from django.test import TestCase
from nose.tools import assert_equal

from pinkflamingo.models import Book, Author, Publisher, Rating


class TestBooks(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Óoly Y')
        self.publisher = Publisher.objects.create(name='Samsara')
        self.book = Book.objects.create(title='The Road of the Rune', isbn='1234567890123', publisher=self.publisher)
        self.user = User.objects.create_user(username="A Reader", email="hi@example.com", password="h0wdy**")


    def test_average_rating(self):
        """book.average_rating should return the average rating of the book"""
        expected_rating = 2.5

        Rating.objects.create(book=self.book, user=self.user, rating=1)
        Rating.objects.create(book=self.book, user=self.user, rating=1)
        Rating.objects.create(book=self.book, user=self.user, rating=5)

        assert_equal(expected_rating, self.book.average_rating)
