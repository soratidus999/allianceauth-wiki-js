# Generated by Django 2.2.12 on 2020-06-11 10:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiJsUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='wikijs', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('uid', models.BigIntegerField()),
            ],
            options={
                'permissions': (('access_wikijs', 'Can access the WikiJS service'),),
            },
        ),
    ]
