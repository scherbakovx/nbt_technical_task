from django.contrib import admin

from api.models import Company, Device, Measurement

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', )


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'company', 'active', 'labels', )
    list_filter = ('company', )
    list_select_related = ('company', )


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('device', 'date', 'data', )
    list_select_related = ('device', )

admin.site.register(Company, CompanyAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Measurement, MeasurementAdmin)
