from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from portxpress.users.models import Agent, Transporter
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    agents = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    transporters = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    # def create(self, validated_data):
    #     """
    #     Validate user on create instance
    #     """
    #     user = User.objects.create_user(**validated_data)
    #     return user
    
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "company_name",
            "tel",
            "bank_name",
            "acc_no",
            "acc_name",
            "balance",
            "email", 
            "url",
            "agents",
            "transporters",
            "password",
            "terms",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "username": {"validators": [UnicodeUsernameValidator()]},
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class AgentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True, partial=True)
        
    class Meta:
        model = Agent
        fields = [
            "user",
            "photo",
            "url"
        ]

        extra_kwargs = {
            "url": {"view_name": "api:agent-detail", "lookup_field": "user_id"}
        }

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        agent, created = Agent.objects.update_or_create(user=user, photo=validated_data.pop("photo"))
        return agent

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        users = UserSerializer(instance=instance.user, data=user_data)
        instance.photo = validated_data.get('photo', instance.photo)
        if users.is_valid():
            users.save()
        instance.save()
        return instance

class TransporterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
        
    class Meta:
        model = Transporter
        fields = [
            "user",
            "photo",
            "vehicle",
            "plate_no",
            "url"
        ]


        extra_kwargs = {
            "url": {"view_name": "api:transporter-detail", "lookup_field": "user_id"}
        }

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        transporter, created = Transporter.objects.update_or_create(user=user, photo=validated_data.pop("photo"), vehicle=validated_data.pop("vehicle"), plate_no=validated_data.pop("plate_no"))
        return transporter

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        users = UserSerializer(instance=instance.user, data=user_data)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.vehicle = validated_data.get('vehicle', instance.vehicle)
        instance.plate_no = validated_data.get('plate_no', instance.plate_no)
        if users.is_valid():
            users.save()
        instance.save()
        return instance

