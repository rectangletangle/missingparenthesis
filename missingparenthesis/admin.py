

from django.contrib import admin
from missingparenthesis.models import Article, Image

class ArticleAdmin (admin.ModelAdmin) :
    list_display = ('title', 'author', 'date')

class ImageAdmin (admin.ModelAdmin) :
    list_display = ('name', 'author', 'date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Image, ImageAdmin)

