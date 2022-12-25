from django.db import models
from django.contrib.auth.models import User

from django.conf.urls.static import static
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
 

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
    
    class meta:
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=150)
    body = RichTextUploadingField(blank=True, null=True,
                                        config_name='special',
                                        external_plugin_resources=[(
                                            'youtube',
                                            '/static/ckeditor_plugins/youtube/youtube/',
                                            'plugin.js',
                                            )],
                                )
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

    class meta:
        ordering =['-date']
        verbose_nama_plural = "Artikel"

class Berita(models.Model):
    
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    konten = models.TextField()
    date = models.CharField(max_length=100)
    gambar = models.CharField(max_length=100)

    def __str__(self) :
        return "{}" - "{}".format(self.nama, self.judul)
