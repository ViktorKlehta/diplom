from django.contrib import admin
from .models import RealEstate


class EstateModelAdmin (admin.ModelAdmin):
    list_display = ['type', 'room_count', 'total_area']
    class Meta:
        model=RealEstate

admin.site.register(RealEstate, EstateModelAdmin)