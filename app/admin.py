from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Theme)
admin.site.register(Quest)