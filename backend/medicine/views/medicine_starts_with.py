from medicine.models import MedicineModel
from medicine.serializers import MedicineModelSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class MedicineStartsWith(APIView):
    """Filter by start letter"""

    def get(self, request):
        medicine_starts_with = request.query_params.get("medicine_starts_with")

        if len(medicine_starts_with) > 1:
            return Response({"message": f"request string length is {len(medicine_starts_with)}"})
        else:    
            medicine = MedicineModel.objects.filter(name__startswith=medicine_starts_with)
            serializer = MedicineModelSerializer(medicine, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
