from psutil import users
from rest_framework import serializers
from myadmin import models
from django.contrib.auth.models import User



class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"

class PackagesSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Packages
        fields = "__all__"        

class UserSerialize(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user