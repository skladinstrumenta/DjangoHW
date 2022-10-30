from django.contrib import admin

from .models import Author, Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'genres')

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
