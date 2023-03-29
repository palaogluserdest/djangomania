from django.contrib import admin
from blog.models import Post, BlogCategory, BlogTag

class PostAdmin(admin.ModelAdmin):
    list_display=[
        'pk',
        'title',
        'content',
        'category',
        'user',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_display_links=[
        'title',
    ]

class BlogCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(BlogCategory)
admin.site.register(BlogTag)
