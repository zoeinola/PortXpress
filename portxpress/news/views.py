from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    FormMixin,
    UpdateView
)
from datetime import datetime

from .models import News, Traffic
from .forms import NewsCreationForm, TrafficCreationForm
# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = "news/list.html"
    ordering = "-pub_date"
    queryset = News.objects.all()
    context_object_name = "news"
    paginate_by = 20
    allow_ampty = True

news_list_view = NewsListView.as_view()

class NewsDetailView(DetailView):
    model = News
    slug_field = "slug"
    slug_url_kwarg = "slug"

news_detail_view = NewsDetailView.as_view()

class TrafficListView(ListView):
    model = News
    template_name = "traffic/list.html"
    ordering = "-pub_date"
    queryset = Traffic.objects.all()
    context_object_name = "traffic"
    paginate_by = 20
    allow_ampty = True

traffic_list_view = TrafficListView.as_view()

class TrafficDetailView(DetailView):
    model = News
    slug_field = "slug"
    slug_url_kwarg = "slug"

traffic_detail_view = TrafficDetailView.as_view()
