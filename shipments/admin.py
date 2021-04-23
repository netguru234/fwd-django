from django.contrib import admin
from .models import Shipment, History


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("tracking_number", "receiver_name", "receiver_address",
                    "receiver_city", "receiver_state", "receiver_country", "sender_name", "sender_address", "sender_city", "sender_state", "sender_country")


admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(History)
