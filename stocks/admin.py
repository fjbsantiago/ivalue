from django.contrib import admin

from .forms import StockModelForm
from .models import Stock

#admin.site.register(Stock)

class StockModelAdmin(admin.ModelAdmin):
    # Allows control over what fields to show, form level validation, etc...
    form = StockModelForm

    class  Meta:
        model = Stock

admin.site.register(Stock, StockModelAdmin)
