# Generated by Django 4.1.4 on 2022-12-20 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0003_alter_artikel_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='nama',
            field=models.CharField(max_length=255, null=True),
        ),
    ]