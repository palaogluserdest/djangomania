from django.contrib import admin
from blog.models import Post, BlogCategory, BlogTag

class PostAdmin(admin.ModelAdmin):
    list_display=[
        'pk',
        'user',
        'title',
        'slug',
        'count',
        'category',
        'is_active',
    ]
    list_display_links=[
        'title',
    ]

class BlogCategoryAdmin(admin.ModelAdmin):
    pass

class BlogTagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(BlogCategory)
admin.site.register(BlogTag)
