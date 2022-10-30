from django.contrib import admin
from .models import Author, Book, User


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_public')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User)
