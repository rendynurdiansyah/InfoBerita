# Generated by Django 4.1.4 on 2022-12-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0008_berita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
