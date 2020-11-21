from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import RequestSerializer
from portxpress.request.models import Request

class RequestViewSet(ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    lookup_field = "slug"
    permission_classes = [IsAdminUser]

    # def get_queryset(self, *args, **kwargs):
    #     if self.status == "ONGOING":
    #         self.transporter = self.request.user
    #         return self.transporter

    # @action(detail=True, methods=["GET"])
    # def me(self, request):
    #     serializer = NewsSerializer(request.user, context={"request": request})
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
