from .dynamic_serializer import DynamicFieldsModelSerializer
from ..models.activity import Activity


class ActivitySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
            "account",
            "title",
        ]
