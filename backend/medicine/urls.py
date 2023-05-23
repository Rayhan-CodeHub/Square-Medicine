from django.urls import path
from medicine.views.filter_by_trade_name import MedicineFilterByTradeNameView
from medicine.views.create_medicine import CreateMedicineView
from medicine.views.medicine_starts_with import MedicineStartsWith


urlpatterns = [
    # http://127.0.0.1:8000/medicine/medicine-filter-by-trade-name/
    path(
        route="medicine-filter-by-trade-name/",
        view=MedicineFilterByTradeNameView.as_view(),
        name="medicine_filter_by_trade_name",
    ),
    
    # http://127.0.0.1:8000/medicine/list-create-medicine/
    path(
        route="list-create-medicine/",
        view = CreateMedicineView.as_view(),
        name="list_create_medicine"
    ),

    # http://127.0.0.1:8000/medicine/medicine-starts-with/
    path(
        route="medicine-starts-with/",
        view = MedicineStartsWith.as_view(),
        name="medicine_starts_with"
    ),
]
