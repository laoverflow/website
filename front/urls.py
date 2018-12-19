from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('get_meetup_members', views.get_meetup_members, name='get_meetup_members')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)