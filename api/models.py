from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author', related_name='books')
    description = models.TextField(blank=True)
    publisher = models.ForeignKey('Publisher')
    isbn = models.CharField(max_length=255)

    def __unicode__(self):
        return "{} - {}".format(self.title, self.authors.all())


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey('auth.User', related_name='ratings_user')
    book = models.ForeignKey('Book', related_name='ratings_book')

    def __unicode__(self):
        return "{} - {} by {}".format(self.rating, self.book, self.user)


