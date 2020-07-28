from django.contrib import admin
from . import models


@admin.register(models.Cue)
class CueAdmin(admin.ModelAdmin):

    list_display = (
        "isButt",
        "isShaft",
        "productName",
        "productNumber",
        "purchasedCustomer",
        "purchasedDate",
        "warrantyNumber",
        "warrantyDate",
        "warrantyManager"
    )

