from django.contrib import admin

from .models import Contest


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ['title']
