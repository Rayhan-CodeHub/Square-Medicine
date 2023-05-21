from django.urls import path
from medicine.views.filter_by_trade_name import MedicineFilterByTradeNameView


urlpatterns = [
    # http://127.0.0.1:8000/medicine/medicine-filter-by-trade-name/
    path(
        route="medicine-filter-by-trade-name/",
        view=MedicineFilterByTradeNameView.as_view(),
        name="medicine_filter_by_trade_name",
    ),
]
