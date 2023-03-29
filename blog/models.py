from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Third Party App:
from autoslug import AutoSlugField
from tinymce.models import HTMLField


class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         # Buradaki adlandırma path kısmında verilen name bilgisdir.
    #         'todo:category_view',
    #         kwargs={
    #             "category_slug": self.slug
    #         }
    #     )


class BlogTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         'todo:tag_view',
    #         kwargs={
    #             "tag_slug": self.slug
    #         }
    #     )


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField(blank=True, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(BlogTag,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='blog_image')
    count=models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #             'todo:todo_detail_view',
    #         kwargs={
    #             "id": self.pk,
    #                 "category_slug": self.category.slug,
    #         }
    #     )


