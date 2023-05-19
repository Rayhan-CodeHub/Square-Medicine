from django.contrib import admin

from .models import MedicineModel

class MedicineModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "group",
        "trade_name",
        "price",
        "mg",
        "medicine_image",
    )


admin.site.register(MedicineModel, MedicineModelAdmin)
