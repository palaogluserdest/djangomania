from django.shortcuts import render, get_object_or_404
from blog.models import Post, BlogCategory, BlogTag
from django.core.paginator import Paginator


def all_post_view(request):
    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')
    all_posts = Post.objects.filter(is_active=True).order_by('-created_at')

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = dict(
        categories=categories,
        tags=tags,
        posts=posts,
        post_count=all_posts.count,
    )
    return render(request, 'blog/all_posts.html', context)


def category_view(request, category_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')
    all_posts = Post.objects.filter(category=category, is_active=True).order_by('-created_at')

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = dict(
        category=category,
        categories=categories,
        tags=tags,
        posts=posts,
        post_count=all_posts.count,
        active_slug=category.slug
    )
    return render(request, 'blog/all_posts.html', context)

def tag_view(request, tag_slug):
    tag= get_object_or_404(BlogTag, slug=tag_slug)
    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')
    posts = Post.objects.filter(
        tag=tag,
        is_active=True
        ).order_by('-created_at')

    context = dict(
        tag=tag,
        categories=categories,
        tags=tags,
        posts=posts,
        active_slug=tag.slug,
    )
    return render(request, 'blog/all_posts.html', context)

def post_detail_view(request, post_slug, category_slug):
    post = get_object_or_404(Post, slug=post_slug)

    # Posta bakılma sayısını tuttuk.
    post.count = post.count + 1
    post.save()

    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')
    context = dict(
        post=post,
        categories=categories,
        category=post.category,
        tags=tags,
    )
    return render(request, 'blog/post_detail.html', context)