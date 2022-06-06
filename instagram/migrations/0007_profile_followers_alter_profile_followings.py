# Generated by Django 4.0.5 on 2022-06-06 08:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0006_profile_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='owers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='ings', to=settings.AUTH_USER_MODEL),
        ),
    ]
