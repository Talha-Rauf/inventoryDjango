from django.contrib import admin
from myApp.models import Inventory, User, AccessRecord

# Register your models here.
admin.site.register(Inventory)
admin.site.register(User)
admin.site.register(AccessRecord)
