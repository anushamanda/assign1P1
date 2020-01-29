from django.contrib import admin
from .models import Tripadvisor

class tripadvisoradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'mail_id')

admin.site.register(Tripadvisor, tripadvisoradmin)
