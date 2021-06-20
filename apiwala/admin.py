from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(ApiPermissions)
admin.site.register(CustomUserModel)
admin.site.register(SubscriptionType)
admin.site.register(UserData)

admin.site.site_title = "Welcome Developer to APIWALA"

admin.site.site_header = "APIWALA DEVELOPER ZONE"

admin.site.index_title = "APIWALA"