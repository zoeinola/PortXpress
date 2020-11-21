# Generated by Django 3.0.10 on 2020-11-21 21:36

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=500, null=True, verbose_name='Request Title')),
                ('destination', models.CharField(max_length=500, null=True, verbose_name='Delivery Destination')),
                ('slug', models.SlugField(blank=True, max_length=600, null=True, unique=True)),
                ('pub_date', models.DateField(null=True, verbose_name='Request Published Date')),
                ('draft', models.BooleanField(default=False)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('distance', models.PositiveIntegerField(verbose_name='Estimated Distance for delivery')),
                ('time', models.TimeField(verbose_name='Estimated Time for delivery')),
                ('status', models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('ONGOING', 'ONGOING'), ('COMPLETED', 'COMPLETED')], default='PENDING', max_length=10, null=True)),
                ('transporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
                'ordering': ['title', '-created'],
                'managed': True,
            },
        ),
    ]
