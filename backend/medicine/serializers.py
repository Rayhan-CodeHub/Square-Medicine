from rest_framework.serializers import ModelSerializer

from .models import MedicineModel


class MedicineModelSerializer(ModelSerializer):
    class Meta:
        model = MedicineModel
        fields = "__all__"
        