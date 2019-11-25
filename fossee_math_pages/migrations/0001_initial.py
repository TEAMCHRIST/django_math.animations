# Generated by Django 2.2 on 2019-11-25 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_days', models.IntegerField(default=0)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_intern', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=255)),
                ('activation_key', models.CharField(blank=True, max_length=255, null=True)),
                ('key_expiry_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
