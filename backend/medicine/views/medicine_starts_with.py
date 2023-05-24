from medicine.models import MedicineModel
from medicine.serializers import MedicineModelSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class MedicineStartsWith(APIView):
    """Filter by start letter"""

    def check_query_parms_length(self, medicine_starts_with):
        if len(medicine_starts_with) == 1:
            return True
        else:
            return False

    def get(self, request):
        medicine_starts_with = request.query_params.get("medicine_starts_with")

        check_query_params_length = self.check_query_parms_length(medicine_starts_with)

        if check_query_params_length:
            medicine = MedicineModel.objects.filter(name__startswith=medicine_starts_with)
            serializer = MedicineModelSerializer(medicine, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                "query_params": f"{medicine_starts_with}", 
                "length": f"{len(medicine_starts_with)}",
                "message": "query_params length should be 1"
            })
            