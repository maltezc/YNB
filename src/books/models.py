# Create your models here.
from django.conf import settings
from django.db import models


def upload_book_image(instance, filename):
    return "books/{user}/{filename}".format(user=instance.user, filename=filename)


class BooksQuerySet(models.QuerySet):
    pass


class BooksManager(models.Manager):
    def get_queryset(self):
        return BooksQuerySet(self.model, using=self._db)


class Books(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL) # user instance .save
    title           = models.TextField()
    author          = models.TextField()
    content         = models.TextField(null=True, blank=True)
    rentalRate      = models.IntegerField()
    location        = models.CharField(max_length=240)
    image           = models.ImageField(upload_to=upload_book_image, null=True, blank=True) # great 3rd part package = django storanges --> AWS#pip install pillow to handle images
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    condition       = models.CharField(null=True, blank=True, max_length=240)


    objects = BooksManager

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


    @property
    def owner(self):
        return self.user
