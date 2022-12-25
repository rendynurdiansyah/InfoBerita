from django.urls import path ,include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('Artikel/',artikel, name='tabel_artikel'),
    path('Berita/',berita, name='tabel_berita'),
    path('tambah_berita/',tambah_artikel, name='tambah_berita'),
    path('artikel/lihat/<str:id>',lihat_artikel,name='lihat_artikel'),
    path('artikel/edit/<str:id>',edit_artikel,name='edit_artikel'),
    path('artikel/delete/<str:id>',delete_artikel,name='delete_artikel'),
    path('users/',users, name='tabel_users'),
    path('sinkron_berita/', sinkron_berita ,name='sinkron_berita') 
] 
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, decument_root = settings.MEDIA_ROOT)