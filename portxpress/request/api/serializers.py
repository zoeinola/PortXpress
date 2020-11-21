from django.contrib.auth import get_user_model

from rest_framework import serializers
from portxpress.request.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            "title",
            "destination",
            "transporter",
            "pub_date",
            "draft",
            "description",
            "distance",
            "time",
            "status",
            "completed_date",
            "cost",
            "overdue_status",
            "url"
        ]

        extra_kwargs = {
            "url": {"view_name": "api:request-detail", "lookup_field": "slug"}
        }

