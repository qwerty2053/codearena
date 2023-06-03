from django.contrib import admin

from .models import Language, Submission


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    ...


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    ...
