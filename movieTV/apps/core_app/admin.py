from django.contrib import admin
from core_app.models import User, UsedMovie
from django.contrib.auth.admin import UserAdmin

# # Register your models here.
class WebUserAdmin(admin.ModelAdmin):
    readonly_fields = (
        'password',
        'series_watched',
        )

# Register your models here.
admin.site.register(User, WebUserAdmin)
admin.site.register(UsedMovie, admin.ModelAdmin)
