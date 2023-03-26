from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'slug',
        'title',
        'content',
        'is_active',
        'created_at',
        'updated_at',
    ]






admin.site.register(Page, PageAdmin,)
