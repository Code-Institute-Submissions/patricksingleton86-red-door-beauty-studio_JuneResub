from django.contrib import admin
from .models import Service, Treatment

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'treatment',
        'price',
    )

    ordering = ('treatment',)

class TreatmentAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'image',
    )

admin.site.register(Service, ServiceAdmin)
admin.site.register(Treatment, TreatmentAdmin)
