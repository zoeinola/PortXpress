from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from portxpress.users.models import Agent, Transporter
from portxpress.users.forms import UserChangeForm, UserCreationForm, AgentSignUpForm, TransporterSignUpForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("company_name", "bank_name", "acc_name", "acc_no", "tel", "terms", "agent", "transporter")}),) + tuple(
        auth_admin.UserAdmin.fieldsets
    )
    list_display = ["username", "company_name", "bank_name", "acc_no", "acc_name", "is_active", "agent", "transporter", "is_superuser"]
    search_fields = ["username", "first_name", "last_name", "bank_name"]
    list_editable = ["bank_name", "acc_no", "acc_name", "agent", "transporter"]


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    add_form = AgentSignUpForm
    list_display = ["__str__", "photo"]
    list_editable = ["photo"]
    
@admin.register(Transporter)
class TransporterAdmin(admin.ModelAdmin):
    add_form = TransporterSignUpForm
    list_display = ["__str__", "photo", "vehicle", "plate_no"]
    list_editable = ["photo", "vehicle", "plate_no"]
