from django.contrib import admin
from order.models import UserOrder
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(UserOrder)
class UserOrderAdmin(ImportExportModelAdmin):
    ordering=['order_id']
    list_display =("order_id","owner","cart_ids","product_ids","invoice_id","payment_status","processed_on")