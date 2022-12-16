from django.contrib import admin
from .models import TrackingModel, PersonalAccount
from django.contrib.auth.models import User

admin.site.register(TrackingModel)
admin.site.register(PersonalAccount)
# admin.site.register(User)

