from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'population', 'created_at')
    search_fields = ('name', 'country')
    list_filter = ('country',)

admin.site.register(City, CityAdmin) 