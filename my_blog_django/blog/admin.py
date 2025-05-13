from django.contrib import admin
from .models import Article, Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'group')
    list_filter = ('group', 'date_added')
    search_fields = ('title', 'content')