from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True)
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='page_image')
    content = models.TextField(blank=True, null=True)
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
