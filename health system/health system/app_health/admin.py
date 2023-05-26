from django.contrib import admin
from app_health.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(doctor_User)
admin.site.register(disease_User)
admin.site.register(medicine_User)
# admin.site.register(cart)
@admin.register(cart)
class cartAdmin(admin.ModelAdmin):
    list_display=['id','medicine','quantity','total']
    # list_display=all
