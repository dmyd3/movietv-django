from django.contrib import admin
from core_app.models import WebUser

# # Register your models here.
# class WebUserAdmin(admin.ModelAdmin):
#     readonly_fields = (
#         #'used_common_names', 'unused_common_names',
#         )

# Register your models here.
admin.site.register(WebUser, admin.ModelAdmin)
