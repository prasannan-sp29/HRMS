# Generated by Django 5.0 on 2024-05-16 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetials',
            name='dept',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
