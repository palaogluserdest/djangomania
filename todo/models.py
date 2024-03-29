from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class TodoCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            # Buradaki adlandırma path kısmında verilen name bilgisdir.
            'todo:category_view',
            kwargs={
                "category_slug": self.slug
            }
        )


class TodoTag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'todo:tag_view',
            kwargs={
                "tag_slug": self.slug
            }
        )


class Todo(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE) # Bu yapıda Category silinmesi durumunda altındaki TODO'larda silinecektir.
    # Bu yapıda ise Category silinmesi durumunda İlgili TODO'ların category'leri Null olarak değişir.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(TodoCategory, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(TodoTag,)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
                'todo:todo_detail_view',
            kwargs={
                "id": self.pk,
                    "category_slug": self.category.slug,
            }
        )
