from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('',views.index,name='index'),
    path('book',views.book,name='book'),
    path('bookingform',views.bookingform,name='bookingform'), 
    path('main', views.main,name='main'),
    path('index',views.index,name='index'),
    path('landing2',views.landing2,name='landing2'),
    path('profile',views.profile,name='profile')
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)