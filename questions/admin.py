from django.contrib import admin
from .models import Category, Question
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'category']
    list_filter = ['category', ]
    search_fields = ['question', 'category']
    list_per_page = 10
