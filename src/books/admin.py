from django.contrib import admin

from .forms import BookForm
from .models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'title',
        '__str__',
        'image',
    ]


    form = BookForm

    class Meta:
        model = Books


admin.site.register(Books, BooksAdmin)

