from rest_framework.generics import ListAPIView
from rest_framework.validators import ValidationError

from medicine.models import MedicineModel
from medicine.serializers import MedicineModelSerializer

class MedicineFilterByTradeNameView(ListAPIView):
    """medicine can filter by trade name"""

    serializer_class = MedicineModelSerializer

    def check_trade_name(self, trade_name):
        if trade_name:
            return True
        else:
            return False

    def get_queryset(self):
        trade_name = self.request.query_params.get("trade_name")
        check_trade_name = self.check_trade_name(trade_name)
        if check_trade_name:
            queryset = MedicineModel.objects.filter(trade_name=trade_name)
            if queryset:
                return queryset
            else:
                raise ValidationError({
                    "details": f"{trade_name} doesn't exceeded"
                })
        else:
            raise ValidationError({
                "details": "trade name is required"
            })
    