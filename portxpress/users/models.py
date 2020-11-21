import os
import random

from django.contrib.auth.models import AbstractUser
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
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def agent_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "agents/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

def transporter_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "transporter/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class User(AbstractUser):
    """Default user for portxpress."""

    #: First and last name do not cover name patterns around the globe
    tel = PhoneNumberField(null=True, blank=True)
    company_name = CharField(_("Company Name"), blank=True, max_length=255)
    bank_name = CharField(_("Bank Name"), blank=True, max_length=255)
    acc_name = CharField(_("Account Name"), blank=True, max_length=255)
    acc_no = CharField(_("Account No"), blank=True, max_length=13)
    balance = DecimalField(_("Wallet Balance"), default=0.00, max_digits=18, decimal_places=2, null=True, blank=True)
    terms = BooleanField(default=False)
    agent = BooleanField(default=False)
    transporter = BooleanField(default=False)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Agent(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name="agents")
    photo = ImageField(_('Profile Photo'), upload_to=agent_image_path, null=True, blank=True)

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

    def __str__(self):
        return str(self.user.username)

    



class Transporter(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name="transporters")
    vehicle = CharField(_("Transporter Vehicle"), null=True, blank=True, max_length=255)
    plate_no = CharField(_("Transporter Vehicle Number"), null=True, blank=True, max_length=10)
    photo = ImageField(_('Profile Photo'), upload_to=transporter_image_path, null=True, blank=True)

    class Meta:
        verbose_name = "Transporter"
        verbose_name_plural = "Transporters"

    def __str__(self):
        return str(self.user.username)

    



