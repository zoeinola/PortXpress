import os
import random

from django.conf import settings
from django.utils import timezone
from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    FileField,
    ForeignKey,
    ImageField,
    IntegerField,
    OneToOneField,
    Q,
    SlugField,
    CASCADE,
    SET_NULL,
    URLField,
    Model
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)

from portxpress.utils.unique_slug_generator import unique_slug_generator

from ckeditor_uploader.fields import RichTextUploadingField
from model_utils.models import TimeStampedModel

User = settings.AUTH_USER_MODEL

def blog_file_path(instance, filename):
    return "blog/files/{filename}".format(filename=filename)


class News(TimeStampedModel):
    title = CharField(_('Post Title'), blank=False, null=True, max_length=500)
    slug = SlugField(unique=True, null=True, blank=True, max_length=600)
    image = ImageField(_("Upload Info"), upload_to=blog_file_path, null=True, blank=True)
    pub_date = DateField(_('Post Published Date'), auto_now=False, auto_now_add=False, null=True, blank=False)
    draft = BooleanField(default=False)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['title', '-created']


    def get_absolute_url(self):
        return f"/news/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"


class Traffic(TimeStampedModel):
    title = CharField(_('Post Title'), blank=False, null=True, max_length=500)
    slug = SlugField(unique=True, null=True, blank=True, max_length=600)
    image = FileField(_("Upload Info"), upload_to=blog_file_path, null=True, blank=True)
    pub_date = DateField(_('Post Published Date'), auto_now=False, auto_now_add=False, null=True, blank=False)
    draft = BooleanField(default=False)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Traffic'
        verbose_name_plural = 'Traffics'
        ordering = ['title', '-created']

    def get_absolute_url(self):
        return f"/traffic/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"

