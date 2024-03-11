from django.contrib import admin
from .models import Regex, FormatJson


@admin.register(Regex)
class RegexAdmin(admin.ModelAdmin):
    list_display = ['name', 'regex', 'active']
    list_editable = ['regex', 'active']
    list_filter = ['active']
    search_fields = ['regex']


@admin.register(FormatJson)
class FormatJsonAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
