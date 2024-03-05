from django.contrib import admin
from contactenquiry.models import contactEnquiry

class  contactadmin(admin.ModelAdmin):
    list_display=('name','email','phone')

admin.site.register(contactEnquiry,contactadmin)

# Register your models here.
