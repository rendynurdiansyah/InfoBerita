# Generated by Django 4.1.4 on 2022-12-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0006_alter_artikel_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
