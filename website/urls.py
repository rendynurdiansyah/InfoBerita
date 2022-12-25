from django.contrib import admin
from django.urls import path ,include
from . views import *
from django.conf import settings

from website import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404,handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('berita.urls')),
    path('', index, name='index'),
    path('artikel/<int:id>/detail/', detail_artikel, name='detail_artikel'),
    path('blog', blog, name='blog'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('artikel', artikel, name='artikel'),

    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
] 
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, decument_root = settings.MEDIA_ROOT)