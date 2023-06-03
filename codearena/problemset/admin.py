from django.contrib import admin
from .models import Tag, Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
