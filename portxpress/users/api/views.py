from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import UserSerializer, AgentSerializer, TransporterSerializer
from portxpress.users.models import Agent, Transporter
User = get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    permission_classes = [IsAdminUser]

    # def get_queryset(self, *args, **kwargs):
    #     return self.queryset.filter(id=self.request.user.id)

    @action(detail=True, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class AgentViewSet(ModelViewSet):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()
    lookup_field = "user_id"
    permission_classes = [IsAdminUser]

    # def get_queryset(self, *args, **kwargs):
    #     return self.queryset.filter(user__id=self.request.user.id)

    @action(detail=True, methods=["GET"])
    def me(self, request):
        agent=self.get_object()
        serializer = AgentSerializer(agent, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    @action(detail=False, methods=["POST"])
    def set_user(self, request, user__username=None):
        agent = self.get_object()
        serializer = AgentSerializer(data=request.data)#, context={"request": request})
        if serializer.is_valid(raise_exception=ValueError):
            agent.user(serializer.data["user"])
            agent.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


class TransporterViewSet(ModelViewSet):
    serializer_class = TransporterSerializer
    queryset = Transporter.objects.all()
    lookup_field = "user_id"
    permission_classes = [IsAdminUser]

    # def get_queryset(self, *args, **kwargs):
    #     return self.queryset.filter(user__id=self.request.user.id)

    @action(detail=True, methods=["GET"])
    def me(self, request):
        transporter=self.get_object()
        serializer = TransporterSerializer(transporter, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    @action(detail=False, methods=["POST"])
    def set_user(self, request, user__username=None):
        transporter = self.get_object()
        serializer = TransporterSerializer(data=request.data)#, context={"request": request})
        if serializer.is_valid():
            transporter.user(serializer.data["user"])
            transporter.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)
