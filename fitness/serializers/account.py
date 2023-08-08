from rest_framework import serializers
from ..models.account import Account
from .activity import ActivitySerializer


class AccountSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = "__all__"
