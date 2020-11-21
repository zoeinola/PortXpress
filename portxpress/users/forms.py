from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.fields.files import ImageField
from django.db import transaction
from django import forms

User = get_user_model()

from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        fields = ["company_name", "username"]
        exclude = ["password"]



class UserCreationForm(admin_forms.UserCreationForm):

    error_message = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "company_name",
            "email",
            "tel",
            "bank_name",
            "acc_no",
            "acc_name",
            "terms",
        ]
        widgets = {
            # "photo": forms.FileInput(attrs={"onchange":"previewImage(this);", "class":"btn btn-block btn-outline-secondary"}),
            "tel": PhoneNumberInternationalFallbackWidget(),
            "terms": forms.CheckboxInput(attrs={"title":"By accepting our terms you agree to abide by our terms of use"})
        }

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class AgentSignUpForm(UserCreationForm):
    photo = forms.ImageField()
    class Meta(UserCreationForm.Meta):
        """
        docstring
        """
        model = User
        widgets = {
            "photo": forms.FileInput(attrs={"onchange":"previewImage(this);", "class":"btn btn-block btn-outline-secondary"}),
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.agent = True
        user.transporter = False
        if commit:
            user.save()
        return user

class TransporterSignUpForm(UserCreationForm):
    photo = forms.ImageField()
    vehicle = forms.CharField(max_length=255, required=False)
    plate_no = forms.CharField(max_length=10, required=False)
    class Meta(UserCreationForm.Meta):
        """
        docstring
        """
        model = User
        widgets = {
            "photo": forms.FileInput(attrs={"onchange":"previewImage(this);", "class":"btn btn-block btn-outline-secondary"}),
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.transporter = True
        user.agent = False
        if commit:
            user.save()
        return user
