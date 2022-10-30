from django.contrib import admin
from .models import Writer, Article, Comment, LikeToArticle, LikeToComment


class WriterAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_public')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_comm')



admin.site.register(Writer, WriterAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(LikeToArticle)
admin.site.register(LikeToComment)

