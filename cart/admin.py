from django.contrib import admin
from .models import Order, Item

# Registering the models
admin.site.register(Order)
admin.site.register(Item)
