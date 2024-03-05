from django.contrib import admin
from services.models import Service
class serviceadmin(admin.ModelAdmin):
    list_display=('service_logo','service_des','service_img','service_head','service_rat')

admin.site.register(Service,serviceadmin)

# Register your models here.
