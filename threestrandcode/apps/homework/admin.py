from django.contrib import admin
from . import models


admin.site.register(models.Assignment)
admin.site.register(models.Recipe)
admin.site.register(models.Path)
admin.site.register(models.Topic)
admin.site.register(models.Course)
