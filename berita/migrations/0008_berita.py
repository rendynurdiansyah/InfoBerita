# Generated by Django 4.1.4 on 2022-12-21 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0007_artikel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('konten', models.TextField()),
                ('date', models.DateField()),
                ('gambar', models.FileField(upload_to='')),
            ],
        ),
    ]
