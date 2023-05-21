from rest_framework.generics import ListAPIView

from medicine.models import MedicineModel
from medicine.serializers import MedicineModelSerializer

class MedicineFilterByTradeNameView(ListAPIView):
    """medicine can filter by trade name"""

    serializer_class = MedicineModelSerializer

    def get_queryset(self):
        trade_name = self.request.query_params.get("trade_name")
        queryset = MedicineModel.objects.filter(trade_name=trade_name)
        return queryset
    