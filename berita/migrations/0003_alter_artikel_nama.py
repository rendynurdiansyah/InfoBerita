# Generated by Django 4.1.4 on 2022-12-20 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('berita', '0002_rename_kategory_artikel_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='nama',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
