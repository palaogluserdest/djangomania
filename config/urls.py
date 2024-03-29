"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pages.views import home_view
from config.views import logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    
    # Blog App'in urls yapısı eklendi.
    path('blog/', include('blog.urls', namespace='blog')),

    # Todo app'nin urls yapısı eklendi.
    path('todo/', include('todo.urls', namespace='todo')),
    
     # Page app'nin urls yapısı eklendi.
    path('page/', include('pages.urls', namespace='page')),
    
    # Auth:
    path('account/logout', logout_view, name="logout_view"),
    # Admin:
    path('admin/', admin.site.urls),

    #Tinymce için path
    path('tinymce/', include('tinymce.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
