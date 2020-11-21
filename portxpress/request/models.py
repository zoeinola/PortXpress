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
    PositiveIntegerField,
    Q,
    TimeField,
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

ONGOING = "ONGOING"
COMPLETED = "COMPLETED"
PENDING = "PENDING"
STATUS = (
    (PENDING, "PENDING"),
    (ONGOING, "ONGOING"),
    (COMPLETED, "COMPLETED"),
)

class Request(TimeStampedModel):
    title = CharField(_('Request Title'), blank=False, null=True, max_length=500)
    destination = CharField(_('Delivery Destination'), blank=False, null=True, max_length=500)
    transporter = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    slug = SlugField(unique=True, null=True, blank=True, max_length=600)
    pub_date = DateField(_('Request Published Date'), auto_now=False, auto_now_add=False, null=True, blank=False)
    draft = BooleanField(default=False)
    description = RichTextUploadingField()
    distance = PositiveIntegerField(_("Estimated Distance for delivery"))
    time = TimeField(_("Estimated Time for delivery"), auto_now=False, auto_now_add=False)
    status = CharField(choices=STATUS, default=PENDING, max_length=10, null=True, blank=True)

    @property
    def completed_date(self):
        if self.status == "COMPLETED":
            return timezone.now()

    @property
    def cost(self):
        if self.distance > 0:
            return Decimal(90.00) * self.distance + 500

    @property
    def overdue_status(self):
        "Returns whether the Tasks's due date has passed or not."
        if self.time and datetime.date.today() > self.time:
            return True

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
        ordering = ['title', '-created']


    def get_absolute_url(self):
        return f"/request/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"

