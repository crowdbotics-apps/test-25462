from django.contrib import admin
from .models import Item, List, Run

admin.site.register(Item)
admin.site.register(Run)
admin.site.register(List)

# Register your models here.
