from django.contrib import admin
from .models import Service, Category

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
