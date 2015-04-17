from django.contrib import admin

from pinkflamingo.models import Book, Publisher, Author, Rating


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Rating)
admin.site.register(Publisher)