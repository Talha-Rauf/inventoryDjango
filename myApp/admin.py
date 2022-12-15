from django.contrib import admin
from myApp.models import Inventory, Users, AccessRecord

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Users)
admin.site.register(AccessRecord)
