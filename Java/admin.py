from django.contrib import admin
from Java import models
# Register your models here.
admin.site.register([
    models.AddData,
    models.Notes
])