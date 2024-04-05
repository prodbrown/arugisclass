from django.contrib import admin
from .models import User


# Register the custom user model with the custom admin class
admin.site.register(User)