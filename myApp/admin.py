from django.contrib import admin

from .models import *

class Custom_User_Display (admin.ModelAdmin):
    list_display=['display_name', 'email']


admin.site.register(Custom_User,Custom_User_Display)
admin.site.register(Workshop_Registration)
admin.site.register(Receive_Service)
admin.site.register(Service_Completion)
admin.site.register(Cancelled_Service)
