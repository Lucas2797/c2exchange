from rest_framework import fields, serializers
from .models import Investiment, Profile
from django.contrib.auth import get_user_model

User = get_user_model()




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'profile']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user',]


class InvestimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investiment
        fields = ['one', 'coin', 'ammount', 'payd']





