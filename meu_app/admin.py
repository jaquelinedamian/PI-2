from django.contrib import admin

# Register your models here.
from .models import Pets

admin.site.register(Pets)