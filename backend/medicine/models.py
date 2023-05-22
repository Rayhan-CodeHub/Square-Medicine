from django.conf import settings

from django.db import models
from django.utils.html import mark_safe

class MedicineModel(models.Model):
    name = models.CharField(max_length=30)
    group = models.CharField(max_length=30)
    trade_name = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField()
    mg = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to="picture/uploads/%Y/%m/%d", null=True, blank=True)

    class Meta:
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"
        db_table = "medicine"

    def medicine_image(self):
        if self.image != "":
            return mark_safe(
                '<img src="{}{}" width=auto height="20" />'.format(
                    f"{settings.MEDIA_URL}", self.image
                )
            )
        
    def __str__(self):
        return self.name
    