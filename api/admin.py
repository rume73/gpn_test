from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Deviation


class DeviationResource(resources.ModelResource):

    class Meta:
        model = Deviation
        fields = ('id', 'shiftnumber', 'region', 'objectid', 'version',
                  'shiftbegt', 'shiftendt', 'attrval_start_weight',
                  'attrval_end_weight', 'acceptance_sum', 'index', 'productid',
                  'shipment_sum')


class DeviationAdmin(ImportExportModelAdmin):
    resource_class = DeviationResource
    list_display = ('index', 'region', 'objectid', 'productid')
    empty_value_display = '-пусто-'


admin.site.register(Deviation, DeviationAdmin)
