# Generated by Django 3.1 on 2020-09-22 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'male gender'), ('Female', 'female gender')], default='Male', max_length=32)),
                ('profile_pic', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[360, 400], upload_to='profile_pic', verbose_name='መለያ ፎቶ')),
                ('bio', models.TextField(blank=True, verbose_name='ባዮ')),
                ('job', models.CharField(blank=True, max_length=26, verbose_name='ስራ')),
                ('telegram', models.CharField(blank=True, max_length=250)),
                ('facebook', models.CharField(blank=True, max_length=250)),
                ('followers', models.ManyToManyField(blank=True, related_name='follow', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]