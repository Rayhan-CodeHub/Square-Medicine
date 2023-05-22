from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response

from medicine.models import MedicineModel
from medicine.serializers import MedicineModelSerializer


class CreateMedicineView(ListCreateAPIView):
    """new medicine can be created & also show the list of medicine"""

    serializer_class = MedicineModelSerializer
    queryset = MedicineModel.objects.all()
