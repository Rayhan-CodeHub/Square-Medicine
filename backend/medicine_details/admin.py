from django.contrib import admin

from .models import MedicineDetailsModel

class MedicineDetailsModelAdmin(admin.ModelAdmin):
    list_display = (
        "indication",
    )

admin.site.register(MedicineDetailsModel, MedicineDetailsModelAdmin)
