from django.urls import path
from todo.views import (
    all_todos_view,
    todo_detail_view,
    category_detail_view,
    tag_detail_view,
)

app_name = 'todo'

urlpatterns = [
    path('', all_todos_view, name="all_todos_view"),
    path('category/<slug:category_slug>/', category_detail_view, name="category_view"),
    path('tag/<slug:tag_slug>/', tag_detail_view, name="tag_view"),
    path('category/<slug:category_slug>/todo/<int:id>/', todo_detail_view, name="todo_detail_view"),
]