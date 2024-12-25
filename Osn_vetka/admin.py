from django.contrib import admin

# Register your models here.
from Osn_vetka import models
admin.site.register(models.Service)
admin.site.register(models.Category)