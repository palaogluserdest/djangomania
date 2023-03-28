from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'content',
        'user',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_display_links=[
        'title',
    ]






admin.site.register(Page, PageAdmin,)
