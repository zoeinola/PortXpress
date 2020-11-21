from django.contrib.auth import get_user_model

from rest_framework import serializers
from portxpress.news.models import News, Traffic


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "title",
            "image",
            "content",
            "pub_date",
            "url"
        ]

        extra_kwargs = {
            "url": {"view_name": "api:news-detail", "lookup_field": "slug"}
        }

class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = [
            "title",
            "image",
            "content",
            "pub_date",
            "url"
        ]

        extra_kwargs = {
            "url": {"view_name": "api:traffic-detail", "lookup_field": "slug"}
        }

