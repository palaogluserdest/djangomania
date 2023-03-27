from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from random import randint
from .fake_db.pages import FAKE_DB_PAGES
from pages.models import Page


FAKE_DB_PROJECTS = [
    f"https://picsum.photos/id/{id}/100/60" for id in range(21, 29)
]

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(24, 28)
]


def home_view(request):
    # print(request)
    # return HttpResponse('Ana sayfaya hos geldiniz...') # Bu sadece bir string ifade donduruyor.
    # context = {"platform": f"Django Platformu kullanildi...randint ile donen veri: {randint(1, 100)}"}
    page_title = "Ana Sayfa"
    hero_title = "Django"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vehicula velit vitae porttitor mollis. Maecenas in purus in leo accumsan viverra non non quam. Curabitur commodo egestas enim, et blandit."
    context = dict(
        page_title=page_title,
        hero_title = hero_title,
        hero_content = hero_content, 
        FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,
    )
    return render(request, "page/index.html", context)



def page_view (request, page_slug):
    page=get_object_or_404(Page, slug=page_slug)
    context=dict(
        page=page,
    )
    return render(request, "page/page_detail.html", context)
    
    