from django.contrib import admin
from . import models


# Register user profile model with django admin
admin.site.register(models.UserProfile)
