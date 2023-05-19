from django.db import models

from medicine.models import MedicineModel

class MedicineDetailsModel(models.Model):
    medicine = models.ForeignKey(MedicineModel, on_delete=models.CASCADE)
    indication = models.TextField(help_text="write indication...")
    dosage = models.TextField()
    preparation = models.TextField()

    class Meta:
        verbose_name = "Medicine Detail"
        verbose_name_plural = "Medicine Details"
        db_table = "medicine_details"
