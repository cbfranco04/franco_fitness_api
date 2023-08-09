from .dynamic_serializer import DynamicFieldsModelSerializer
from ..models.account import Account
from .activity import ActivitySerializer


class AccountSerializer(DynamicFieldsModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = [
            "account_id",
            "username",
            "first_name",
            "activities",
        ]
