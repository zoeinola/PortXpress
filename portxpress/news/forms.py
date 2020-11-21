from django.forms import ModelForm
from .models import News, Traffic
from ckeditor_uploader.widgets import  CKEditorUploadingWidget
import datetime


class NewsCreationForm(ModelForm):
    class Meta:
        model = News
        exclude = ["updated", "created", "slug"]
        widgets = {
            'content': CKEditorUploadingWidget()
        }


class TrafficCreationForm(ModelForm):
    class Meta:
        model = Traffic
        exclude = ["updated", "created", "slug"]
        widgets = {
            'content': CKEditorUploadingWidget()
        }