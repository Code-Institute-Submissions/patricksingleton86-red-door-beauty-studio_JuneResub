from django.contrib import admin
from .models import Style

# Register your models here.

class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
    )

admin.site.register(Style, StyleAdmin)
