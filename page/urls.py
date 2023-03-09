from django.urls import path
from .views import (
    about_us_view,
    contact_us_view,
    home_view,
    vision_us_view,
    page_view,
    
)

urlpatterns = [
    path('', home_view, name='home'),
    # path('hakkimizda/', about_us_view, name='about_us'),
    # path('iletisim/', contact_us_view, name='contact_us'),
    # path('vizyonumuz/', vision_us_view, name='vision_us'),
   
    # Yukaridaki tum path isini artik asagidaki slug path'i ile hallediyoruz
    path('<slug:slug>/', page_view),
]