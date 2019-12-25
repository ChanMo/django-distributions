from django.contrib import admin

from .models import *


class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_android_version_name', 'get_ios_version_name', 'created')
    view_on_site = True


class VersionAdmin(admin.ModelAdmin):
    list_display = ('app', 'platform', 'name', 'number', 'content', 'created')
    list_per_page = 12
    list_filter = ('app', 'platform', 'created')
    search_fields = ('name',)


admin.site.register(App, AppAdmin)
admin.site.register(Version, VersionAdmin)
