# Generated by Django 2.2.8 on 2019-12-29 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fossee_math_pages', '0002_remove_userdetails_user_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
