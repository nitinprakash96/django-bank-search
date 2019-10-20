from django.contrib import admin

from .models import Banks, Branches

# Register the models
admin.site.register((Banks, Branches))