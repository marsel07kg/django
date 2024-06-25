from django.contrib import admin
from . import models


admin.site.register(models.Book)
admin.site.register(models.Rewiews)
admin.site.register(models.Tag)
admin.site.register(models.Library)

# Register your models here.
