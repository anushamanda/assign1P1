from django.contrib import admin
from .models import Place

class placeadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'is_published', 'tripadvisor')
admin.site.register(Place, placeadmin)