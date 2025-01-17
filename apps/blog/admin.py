from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Админ-панель модели записей
    """
    prepopulated_fields = {'slug': ('title',)}      # параметр prepopulated_fields, который позволяет с помощью встроенного JS обрабатывать заголовок в реальном времени, конвертирует даже кириллицу